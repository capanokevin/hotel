import streamlit as st

# Impostazione della pagina per una visualizzazione più ampia e un titolo personalizzato
st.set_page_config(page_title="Hotel Digital Concierge", layout="wide")

# Definizione di uno stile personalizzato usando HTML e CSS
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stButton button {
        background-color: #000000;
        color: #ffffff;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
        border: 2px solid #000000;
        transition: 0.3s ease;
    }
    .stButton button:hover {
        background-color: #ffffff;
        color: #000000;
        border: 2px solid #000000;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
    }
    .title {
        color: #000000;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-top: 0;
        padding: 0;
    }
    .subtitle {
        color: #808080;
        text-align: center;
        font-size: 18px;
        margin-top: -10px;
        margin-bottom: 20px;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-top: 30px;
    }
    .service-box {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #000000;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
    }
    .service-box:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header principale
st.markdown("<h1 class='title'>Hotel Digital Concierge</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Migliora la tua esperienza presso il nostro hotel con servizi digitali personalizzati</p>", unsafe_allow_html=True)

# Layout principale con tre pulsanti centrali
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="service-box">
            <h3 style='text-align:center;'>Servizio in Camera</h3>
            <p style='text-align:center;'>Richiedi tutto ciò di cui hai bisogno, direttamente dalla tua stanza.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Vai alla chat"):
        st.write("Questa è solo una demo non funzionante della chat per il servizio in camera.")

with col2:
    st.markdown(
        """
        <div class="service-box">
            <h3 style='text-align:center;'>Servizi dell'Hotel</h3>
            <p style='text-align:center;'>Esplora i servizi del nostro hotel, dalla spa alla prenotazione di ristoranti.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Scopri i servizi"):
        st.write("Questa pagina ti mostrerà i servizi disponibili, come la spa o il ristorante.")

with col3:
    st.markdown(
        """
        <div class="service-box">
            <h3 style='text-align:center;'>Assistente Virtuale</h3>
            <p style='text-align:center;'>Chatta con il nostro assistente virtuale per ricevere informazioni sulla città e molto altro.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Parla con l'assistente"):
        st.write("Questa è una demo della chat per l'assistente virtuale.")


# Footer minimale
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>© 2024 Hotel Digital Concierge. All rights reserved.</p>", unsafe_allow_html=True)
