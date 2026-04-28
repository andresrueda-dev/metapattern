st.markdown("""
<style>
body {
    background-color: #0f172a;
}
h1, h2, h3 {
    color: #22c55e;
}
.stButton>button {
    background-color: #22c55e;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
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
