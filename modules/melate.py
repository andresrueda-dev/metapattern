import streamlit as st
from utils.generator import generar_melate
from utils.storage import guardar, cargar
from config import DATA_MELATE
from auth import es_pro

def run():
    st.header("Melate PRO")

    limite = 2 if not es_pro() else 10
    cantidad = st.slider("Cantidad", 1, limite, 2)

    if st.button("Generar Melate"):
        resultados = [generar_melate() for _ in range(cantidad)]

        for i, r in enumerate(resultados):
            st.write(f"{i+1}: {r}")

        guardar(DATA_MELATE, resultados)

    st.subheader("Historial")
    df = cargar(DATA_MELATE)
    if not df.empty:
        st.dataframe(df)
