import os
from dotenv import load_dotenv
import pandas as pd
import mysql.connector
from google import genai

load_dotenv()

conexao = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME")
)

auracursor = conexao.cursor()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

pergunta = input("O que você quer consultar? ")
prompt = f"""
Você é um assistente que converte perguntas em português para comandos SQL, usado em um banco de dados hospitalar MySQL.

Schema do banco:
- pacientes(id_paciente, first_name, last_name, id_medico, id_setor, dt_entrada, idade, city)
- medicos(id_medico, first_name, last_name, crm, idade, id_setor)
- consultas(id_consulta, id_paciente, dt_consul, id_medico, tipo_consul)
- setores(id_setor, name_setor, andar_setor)
- cirurgia(id_cirurgia, id_medico, id_paciente, dt_cirurgia, tipo_cirurgia)

Regras:
- Responda APENAS com o comando SQL puro, sem explicações, sem markdown, sem crases.
- Gere apenas comandos SELECT (nunca INSERT, UPDATE, DELETE, DROP).

Pergunta do usuário: {pergunta}
"""
resposta = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

query_gerada = resposta.text.strip()
print("SQl gerada pela IA", query_gerada)

auracursor.close()
conexao.close()