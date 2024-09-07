import streamlit as st
import openai

# Imposta l'API Key di OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Funzione per interrogare GPT direttamente con OpenAI
def chat_with_gpt(user_message):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Il cliente ha scritto: {user_message}\nRispondi cortesemente e prendi l'ordine per la cucina.",
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Configurazione della pagina
st.set_page_config(page_title="Servizio in Camera", layout="centered")

# Simula l'input del QR code per la camera
room_number = 'Camera 01'  # Simuliamo la Camera 01

# Mostrare il numero della camera e il menu fisso
st.title(f"Benvenuto nella {room_number}")
st.write("Siamo qui per prenderti cura di te! Ecco il nostro menu per il servizio in camera:")

# Menu fisso
menu = """
### Menu Servizio in Camera:
- **Spaghetti al Pomodoro** - €12
- **Risotto ai Funghi** - €14
- **Pizza Margherita** - €10
- **Insalata Greca** - €8
- **Tagliata di Manzo** - €18
- **Dessert: Tiramisù** - €6
- **Bevande: Acqua, Vino Rosso, Vino Bianco**
"""
st.markdown(menu)

# Banner fisso in basso per la chat
st.markdown(
    """
    <style>
    .chat-input-container {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #ff6347;
        color: white;
        text-align: center;
        padding: 10px;
    }
    .chat-input {
        width: 85%;
        padding: 10px;
        margin: 10px;
        border-radius: 25px;
        border: none;
    }
    .chat-submit-btn {
        background-color: white;
        color: #ff6347;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        cursor: pointer;
    }
    .chat-expanded {
        position: fixed;
        bottom: 50px;
        left: 0;
        width: 100%;
        height: 40%;
        background-color: white;
        overflow-y: scroll;
        border: 2px solid #ff6347;
        border-radius: 15px;
        display: none;
    }
    .chat-message {
        padding: 10px;
        border-bottom: 1px solid #ddd;
    }
    </style>
    <div class="chat-input-container" id="chat-banner">
        <input type="text" id="chat-input-banner" class="chat-input" placeholder="Scrivi qui il tuo messaggio..." />
        <button class="chat-submit-btn" onclick="expandChat()">Apri Chat</button>
    </div>
    <div id="chat-expanded" class="chat-expanded">
        <div id="chat-messages">
            <!-- Messaggi di chat dinamici appariranno qui -->
        </div>
        <input type="text" id="chat-input-expanded" class="chat-input" placeholder="Scrivi il tuo messaggio..." />
        <button class="chat-submit-btn" onclick="sendMessage()">Invia</button>
    </div>
    <script>
    function expandChat() {
        document.getElementById('chat-expanded').style.display = 'block';
        document.getElementById('chat-input-banner').style.display = 'none';
    }
    function sendMessage() {
        var message = document.getElementById('chat-input-expanded').value;
        var messageBox = document.getElementById('chat-messages');
        if (message) {
            messageBox.innerHTML += '<div class="chat-message"><strong>Tu:</strong> ' + message + '</div>';
            document.getElementById('chat-input-expanded').value = '';
            
            // Invia il messaggio al backend per la risposta GPT (Chiamata a Streamlit)
            fetchMessageFromGPT(message);
        }
    }
    function fetchMessageFromGPT(message) {
        // Streamlit function to call Python backend
        var user_message = {'message': message};
        Streamlit.setComponentValue(user_message);
    }
    </script>
    """,
    unsafe_allow_html=True
)

# Chat dinamica con OpenAI e messaggi
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Funzione per gestire il messaggio inviato dalla chat
if st.experimental_get_query_params().get('message'):
    user_message = st.experimental_get_query_params().get('message')[0]
    assistant_message = chat_with_gpt(user_message)
    
    # Aggiorna la cronologia della chat
    st.session_state['chat_history'].append({
        'user_message': user_message,
        'assistant_message': assistant_message
    })

# Mostra la cronologia della chat in espansione
if len(st.session_state['chat_history']) > 0:
    st.write("<div id='chat-messages'>", unsafe_allow_html=True)
    for chat in st.session_state['chat_history']:
        st.write(f"<div class='chat-message'><strong>Tu:</strong> {chat['user_message']}</div>", unsafe_allow_html=True)
        st.write(f"<div class='chat-message'><strong>Assistente:</strong> {chat['assistant_message']}</div>", unsafe_allow_html=True)
    st.write("</div>", unsafe_allow_html=True)
