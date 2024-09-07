import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import openai
from langchain import LLMChain
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import HumanMessagePromptTemplate

# Imposta l'API Key di OpenAI
openai.api_key = = st.secrets["OPENAI_API_KEY"]

# Dati simulati per mappare i QR code alle camere
camera_qr_mapping = {
    'qr_code_camera_01': 'Camera 01',
    'qr_code_camera_02': 'Camera 02',
    'qr_code_camera_03': 'Camera 03',
    # Continua con altre camere
}

# Funzione per inviare email
def send_order_via_email(order_text, room_number):
    sender_email = "kevin.capano99@gmail.com"
    receiver_email = "matteoomagri@gmail.com"
    password = "Pallmallone1!"

    # Crea l'oggetto email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"Nuova ordinazione dalla {room_number}"

    # Corpo dell'email
    body = f"Ordine ricevuto dalla {room_number}:\n\n{order_text}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Invia l'email
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Errore nell'invio dell'email: {e}")
        return False

# Funzione per interrogare GPT usando il modello GPT-4o-mini
def chat_with_gpt(user_message):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0, api_key=openai.api_key)
    template = '''
    Sei un assistente virtuale per un hotel. Il cliente ha scritto: {eventuale_testo_aggiuntivo}
    Rispondi cortesemente e prendi l'ordine per la cucina.
    '''
    
    user_prompt = PromptTemplate(template=template, input_variables=["eventuale_testo_aggiuntivo"])
    chat_prompt = ChatPromptTemplate.from_messages([HumanMessagePromptTemplate(prompt=user_prompt)])
    
    llm_chain = LLMChain(prompt=chat_prompt, llm=llm, verbose=False)
    result = llm_chain.run({"eventuale_testo_aggiuntivo": user_message})
    
    return result

# Simula l'input del QR code (in un'implementazione reale, questo sarebbe ottenuto dal QR code)
def get_camera_from_qr_code():
    # In un'implementazione reale, questo parametro verrebbe fornito dalla scansione del QR code
    # Simuliamo con una variabile fissa che può essere cambiata per testare camere diverse
    qr_code = st.experimental_get_query_params().get('qr', ['qr_code_camera_01'])[0]
    return camera_qr_mapping.get(qr_code, 'Camera Sconosciuta')

# Configurazione della pagina
st.set_page_config(page_title="Servizio in Camera", layout="centered")

# Ottenere il numero della camera dal QR code
room_number = get_camera_from_qr_code()

# Mostrare il numero della camera
st.title(f"Benvenuto nella {room_number}")
st.write("Siamo qui per prenderti cura di te! Ecco il nostro menu per il servizio in camera:")

# Menu fittizio
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

# Visualizzare il menu
st.markdown(menu)

# Mostrare il banner per la chat
st.markdown(
    """
    <style>
    .chat-banner {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #ff6347;
        color: white;
        text-align: center;
        padding: 10px;
        cursor: pointer;
    }
    </style>
    <div class="chat-banner" onclick="document.getElementById('chat-box').style.display='block';">
        Chatta con noi!
    </div>
    """,
    unsafe_allow_html=True
)

# Area della chat (inizialmente nascosta)
st.markdown(
    """
    <style>
    #chat-box {
        display: none;
        position: fixed;
        bottom: 50px;
        right: 20px;
        width: 300px;
        height: 400px;
        background-color: white;
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 10px;
        overflow-y: scroll;
    }
    </style>
    <div id="chat-box">
        <h4>Assistente Virtuale</h4>
    </div>
    """,
    unsafe_allow_html=True
)

# Se l'utente clicca sulla chat, si apre l'interfaccia della chat
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Visualizzare la cronologia della chat
if st.button("Apri Chat"):
    st.markdown("<script>document.getElementById('chat-box').style.display='block';</script>", unsafe_allow_html=True)
    
    # Mostrare la chat
    for chat in st.session_state['chat_history']:
        st.markdown(f"**Tu:** {chat['user_message']}")
        st.markdown(f"**Assistente:** {chat['assistant_message']}")

    user_input = st.text_input("Scrivi qui il tuo messaggio:")

    if st.button("Invia"):
        if user_input:
            assistant_message = chat_with_gpt(user_input)
            st.session_state['chat_history'].append({
                'user_message': user_input,
                'assistant_message': assistant_message
            })
            st.markdown(f"**Tu:** {user_input}")
            st.markdown(f"**Assistente:** {assistant_message}")

    # Bottone per inviare l'ordine
    if st.button("Invia Ordine"):
        full_order = "\n".join([f"Utente: {chat['user_message']}\nAssistente: {chat['assistant_message']}" for chat in st.session_state['chat_history']])
        if send_order_via_email(full_order, room_number):
            st.success(f"Ordine inviato con successo alla cucina dalla {room_number}!")
        else:
            st.error("Errore nell'invio dell'ordine. Riprova più tardi.")

# Reset della chat
if st.button("Resetta la chat"):
    st.session_state['chat_history'] = []
    st.success("Chat resettata con successo.")
