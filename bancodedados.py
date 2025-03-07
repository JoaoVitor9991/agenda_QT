import mysql.connector
from mysql.connector import Error  

def conectar():
    """Estabelece conexão com o banco de dados MySQL e exibe o erro se falhar."""
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",           
            password="",  
            database="meu_banco"   
        )
        return conexao
    except Error as e:
        print(f"❌ Erro ao conectar ao banco de dados: {e}")  
        return None
