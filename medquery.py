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
auracursor.execute("select * from pacientes where city = 'Caxias do Sul'")

resultado = auracursor.fetchall()
df = pd.DataFrame(resultado, columns = ['id_paciente','first_name','last_name','id_medico','id_setor','dt_entrada','idade','city'])

print(df)

auracursor.close()
conexao.close()