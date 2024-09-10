import streamlit as st
from PIL import Image

# Titolo principale dell'app
st.title('Hotel Digital Concierge')
st.write("Benvenuto nell'app dell'hotel! Seleziona uno dei servizi per continuare.")

# Creiamo la sidebar di navigazione
page = st.sidebar.selectbox("Seleziona un servizio", ["Home", "Servizio in Camera", "Hotel Services", "Virtual Assistant"])

# Home Page
if page == "Home":
    st.header("Benvenuto!")
    st.write("Scegli tra i seguenti servizi per migliorare la tua esperienza presso il nostro hotel.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Servizio in Camera"):
            st.write("Clicca sulla barra laterale per accedere al servizio in camera.")

    with col2:
        if st.button("Hotel Services"):
            st.write("Clicca sulla barra laterale per esplorare i servizi dell'hotel.")

    with col3:
        if st.button("Virtual Assistant"):
            st.write("Clicca sulla barra laterale per parlare con l'assistente virtuale.")

# Pagina Servizio in Camera
elif page == "Servizio in Camera":
    st.header("Servizio in Camera")
    st.write("Chat non funzionante, solo per scopi dimostrativi.")
    
    # Aggiunta di una chat demo
    st.text_area("Chat", "Buonasera! Come posso assisterti con il servizio in camera oggi?", height=200)

# Pagina Hotel Services
elif page == "Hotel Services":
    st.header("Hotel Services")
    st.write("Scopri i servizi offerti dall'hotel.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Prenota il Ristorante")
        st.write("Clicca qui per prenotare un tavolo nel nostro ristorante.")
        st.button("Prenota ora")

        st.subheader("Prenota la Spa")
        st.write("Rilassati nella nostra spa di lusso.")
        st.button("Prenota ora")
    
    with col2:
        st.subheader("Prenota il Servizio Taxi")
        st.write("Richiedi un taxi per esplorare la città.")
        st.button("Richiedi Taxi")

        st.subheader("Lavanderia")
        st.write("Prenota il servizio lavanderia direttamente dalla tua stanza.")
        st.button("Richiedi Servizio")

# Pagina Virtual Assistant
elif page == "Virtual Assistant":
    st.header("Virtual Assistant")
    st.write("Chatta con il nostro assistente virtuale per avere informazioni sull'hotel, sulla città e altro.")

    # Chat demo per assistente virtuale
    query = st.text_input("Come posso aiutarti?")
    
    if query:
        st.write(f"Risposta automatica: Sto cercando informazioni riguardo '{query}'.")

