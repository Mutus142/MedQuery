import os
from dotenv import load_dotenv
import pandas as pd
import mysql.connector

load_dotenv()

conexao = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME")
)

auracursor = conexao.cursor()

# aqui é onde a pergunta do usuário e a IA vão entrar

auracursor.close()
conexao.close()