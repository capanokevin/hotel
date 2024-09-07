import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import openai

# Imposta l'API Key di OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]


# Funzione per interrogare GPT direttamente con OpenAI
def chat_with_gpt(user_message):
    response = openai.Completion.create(
        model="gpt-4o-mini",  
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
        width: 90%;
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
        height: 50%;
        background-color: white;
        overflow-y: scroll;
        border: 2px solid #ff6347;
        border-radius: 15px;
    }
    .chat-message {
        padding: 10px;
        border-bottom: 1px solid #ddd;
    }
    </style>
    <div class="chat-input-container" id="chat-banner">
        <input type="text" class="chat-input" id="chat-input" placeholder="Scrivi qui il tuo messaggio..." />
        <button class="chat-submit-btn" onclick="document.getElementById('chat-box').style.display='block';">Apri Chat</button>
    </div>
    <div id="chat-box" class="chat-expanded" style="display:none;">
        <div id="chat-messages">
            <!-- Messaggi di chat dinamici appariranno qui -->
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Chat dinamica con OpenAI e messaggi
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input utente dalla chat
user_input = st.text_input("Scrivi qui il tuo messaggio", key="chat_input")

if st.button("Invia"):
    if user_input:
        # Simula la risposta di ChatGPT
        assistant_message = chat_with_gpt(user_input)
        # Aggiorna la cronologia della chat
        st.session_state['chat_history'].append({
            'user_message': user_input,
            'assistant_message': assistant_message
        })

# Mostra la cronologia della chat
for chat in st.session_state['chat_history']:
    st.write(f"**Tu:** {chat['user_message']}")
    st.write(f"**Assistente:** {chat['assistant_message']}")

# Bottone per resettare la chat
if st.button("Resetta la chat"):
    st.session_state['chat_history'] = []
    st.success("Chat resettata con successo.")

