import mysql.connector
from mysql.connector import Error  

def conectar():
    """Estabelece conexão com o banco de dados MySQL."""
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",  # Altere se necessário
            password="sua_senha",
            database="meu_banco"
        )
        return conexao
    except Error as e:
        print(f"❌ Erro ao conectar ao banco de dados: {e}")
        return None

def salvar_usuario(email, senha, nome, contato):
    """Insere um novo usuário no banco de dados."""
    conexao = conectar()
    if conexao is None:
        return False

    try:
        cursor = conexao.cursor()

        sql = "INSERT INTO usuarios (nome, email, contato, senha_hash) VALUES (%s, %s, %s, SHA2(%s, 256))"
        valores = (nome, email, contato, senha)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()
        return True
    except mysql.connector.IntegrityError:
        print("Erro: Email já cadastrado!")
        return False
    except Error as e:
        print(f"Erro ao salvar usuário: {e}")
        return False
