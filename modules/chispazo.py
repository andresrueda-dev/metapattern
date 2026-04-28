import streamlit as st
from utils.generator import generar_chispazo
from utils.storage import guardar, cargar
from utils.analysis import calcular_aciertos
from config import DATA_CHISPAZO
from auth import es_pro

def run():
    st.header("Chispazo PRO")

    limite = 2 if not es_pro() else 10
    cantidad = st.slider("Cantidad", 1, limite, 2)

    if st.button("Generar"):
        resultados = [generar_chispazo() for _ in range(cantidad)]

        for i, r in enumerate(resultados):
            st.write(f"{i+1}: {r}")

        guardar(DATA_CHISPAZO, resultados)

    st.subheader("Registrar resultado")
    resultado = st.text_input("Ej: 4,6,11,22,25")

    if st.button("Actualizar"):
        df = cargar(DATA_CHISPAZO)
        df["resultado"] = resultado
        df["aciertos"] = df["numeros"].apply(lambda x: calcular_aciertos(x, resultado))
        df.to_csv(DATA_CHISPAZO, index=False)

    st.subheader("Dashboard")
    df = cargar(DATA_CHISPAZO)
    if not df.empty:
        st.metric("Jugadas", len(df))
        st.metric("Promedio", round(df["aciertos"].mean(), 2))
        st.dataframe(df)
