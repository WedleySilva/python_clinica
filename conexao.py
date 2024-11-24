import mysql.connector
from mysql.connector import Error

# Função para conectar ao banco de dados MySQL
def conectar():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='clinica_esteticadb',
            user='root',
            password=''  # Alterar para sua senha se necessário
        )
        if connection.is_connected():
            print("Conexão com o banco de dados bem-sucedida!")
            return connection
    except Error as e:
        print("Erro ao conectar ao MySQL:", e)
        return None
