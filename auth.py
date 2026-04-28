import streamlit as st
from config import USERS

def login():
    st.sidebar.title("Login")

    user = st.sidebar.text_input("Usuario")
    password = st.sidebar.text_input("Contraseña", type="password")

    if st.sidebar.button("Entrar"):
        if user in USERS and USERS[user] == password:
            st.session_state["user"] = user
            st.success("Acceso concedido")
        else:
            st.error("Datos incorrectos")

def check_auth():
    if "user" not in st.session_state:
        st.warning("Inicia sesión")
        st.stop()

def es_pro():
    return st.session_state.get("user") == "pro_user"
