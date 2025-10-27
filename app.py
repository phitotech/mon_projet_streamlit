import streamlit as st

st.title("Mon application Streamlit")
st.write("Bienvenue dans mon app !")

with open("no.txt", "r") as f:
    contenu = f.read()
    st.text("Contenu de no.txt :")
    st.code(contenu)
