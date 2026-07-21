"""
import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime
import mysql.connector

st.markdown("""
<style>
.stApp {
    background-color: #0a0a0f;
    background-image: radial-gradient(
        circle at center,
        #2e1a47 0%,
        #1a1025 35%,
        #0a0a0f 70%
    );
}
.block-container {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<p style='font-size: 20px; margin: 0;'>MedQuery</p>", unsafe_allow_html=True)

hora_atual = datetime.now().hour
nome_usuario = os.getenv("USERNAME")

if hora_atual < 12:
    saudacao = ("Bom dia,")
elif hora_atual < 18:
    saudacao = ("Boa tarde,")
else:
    saudacao = ("Boa noite,")

st.write(saudacao, nome_usuario)

load_dotenv()

opcoes = [
    "Pacientes de uma Cidade",
    "Médico com mais Consultas",
    "Media de idade dos Pacientes"
]

escolha = st.selectbox("Escolha uma pergunta", opcoes)
"""