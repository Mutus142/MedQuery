import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
import mysql.connector

st.title("MedQuery")
st.write("MedQuery")

load_dotenv()

opcoes = [
    "Pacientes de uma Cidade",
    "Médico com mais Consultas",
    "Media de idade dos Pacientes"
]

escolha = st.selectbox("Escolha uma pergunta", opcoes)

if escolha == "Pacientes de uma Cidade":
    query = "select * from pacientes where city = 'Caxias do Sul'" 

elif escolha == "Médico com mais Consultas":
    query = "SELECT a.first_name, a.id_medico, COUNT(*) AS total_consultas FROM medicos a INNER JOIN consultas b ON a.id_medico = b.id_medico GROUP BY a.id_medico, a.first_name ORDER BY total_consultas DESC"

elif escolha == "Media de idade dos Pacientes":
    query = "select avg(idade) from pacientes"

conexao = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME")
)

auracursor = conexao.cursor()
auracursor.execute(query)

resultado = auracursor.fetchall()

df = pd.DataFrame(resultado, columns = auracursor.column_names)

print(df)

auracursor.close()
conexao.close()