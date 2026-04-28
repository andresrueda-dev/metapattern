import streamlit as st
from auth import login, check_auth
from modules import chispazo, melate

st.set_page_config(page_title="MetaPattern Engine", layout="wide")

login()
check_auth()

st.title("🎯 MetaPattern Engine PRO")

tab1, tab2 = st.tabs(["Chispazo", "Melate"])

with tab1:
    chispazo.run()

with tab2:
    melate.run()
