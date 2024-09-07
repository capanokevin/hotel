import streamlit as st
import openai

# Imposta l'API Key di OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]


# Funzione per interrogare GPT con il menu
def chat_with_gpt(user_message):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Il cliente ha scritto: {user_message}\nRispondi cortesemente e prendi l'ordine per la cucina.",
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Funzione per mostrare il menu automatico all'inizio
def show_menu():
    return """
    Benvenuto nel servizio in camera! Ecco il nostro menu:
    - **Spaghetti al Pomodoro** - €12
    - **Risotto ai Funghi** - €14
    - **Pizza Margherita** - €10
    - **Insalata Greca** - €8
    - **Tagliata di Manzo** - €18
    - **Dessert: Tiramisù** - €6
    - **Bevande: Acqua, Vino Rosso, Vino Bianco**
    Scrivi qui il tuo ordine quando sei pronto!
    """

# Configurazione della pagina
st.set_page_config(page_title="Hotel Assistant", layout="centered")

# Pagina principale con tre opzioni
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

if st.session_state['page'] == 'home':
    st.title("Benvenuto nel nostro Hotel")
    st.write("Seleziona un'opzione per continuare:")
    
    # Stile CSS per i box
    st.markdown("""
    <style>
    .option-box {
        display: inline-block;
        width: 100%;
        margin: 10px 0;
        padding: 20px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: white;
        border-radius: 10px;
        cursor: pointer;
    }
    .room-service { background-color: #ff6347; }
    .hotel-services { background-color: #00bfff; }
    .concierge { background-color: #32cd32; }
    .option-box:hover { opacity: 0.8; }
    </style>
    """, unsafe_allow_html=True)

    # Box per Room Service
    st.markdown('<div class="option-box room-service" onclick="window.location.href = \'#\'">Room Service</div>', unsafe_allow_html=True)
    # Box per Servizi dell'Hotel (non funzionante nella demo)
    st.markdown('<div class="option-box hotel-services">Servizi dell\'Hotel</div>', unsafe_allow_html=True)
    # Box per Concierge (non funzionante nella demo)
    st.markdown('<div class="option-box concierge">Concierge</div>', unsafe_allow_html=True)

    # Interazione con il box cliccato
    if st.button("Room Service"):
        st.session_state['page'] = 'room_service'

# Pagina Room Service (chat)
if st.session_state['page'] == 'room_service':
    st.title("Room Service Chat")

    # Inizializzazione della cronologia della chat
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
        # Il chatbot invia automaticamente il menu al primo accesso
        st.session_state['chat_history'].append({
            'assistant_message': show_menu()
        })

    # Funzione per visualizzare la cronologia della chat in stile WhatsApp/Telegram
    def display_chat():
        for chat in st.session_state['chat_history']:
            if 'user_message' in chat:
                st.markdown(f"<div style='background-color:#dcf8c6;padding:10px;border-radius:10px;margin:5px 0;text-align:right;color:black;'>**Tu:** {chat['user_message']}</div>", unsafe_allow_html=True)
            if 'assistant_message' in chat:
                st.markdown(f"<div style='background-color:#ececec;padding:10px;border-radius:10px;margin:5px 0;text-align:left;color:black;'>**Assistente:** {chat['assistant_message']}</div>", unsafe_allow_html=True)

    # Mostra la cronologia della chat
    display_chat()

    # Input utente per la chat
    user_input = st.text_input("Scrivi qui il tuo messaggio", key="chat_input")

    if st.button("Invia"):
        if user_input:
            # Invia il messaggio dell'utente e ottieni la risposta dall'assistente
            assistant_message = chat_with_gpt(user_input)
            # Aggiungi i messaggi alla cronologia
            st.session_state['chat_history'].append({
                'user_message': user_input,
                'assistant_message': assistant_message
            })
            # Aggiorna la pagina per mostrare i nuovi messaggi
            st.experimental_rerun()
