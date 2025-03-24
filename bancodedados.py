import mysql.connector
from datetime import datetime
import sqlite3

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Ajuste conforme sua configuração
            database="agenda"
        )
        return conexao
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

def criar_tabela_usuarios():
    conexao = conectar()
    if conexao is None:
        print("Erro ao conectar ao banco.")
        return

    cursor = None
    try:
        cursor = conexao.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                contato VARCHAR(20),
                senha_hash VARCHAR(256) NOT NULL,
                foto BLOB
            )
        """
        cursor.execute(sql)
        conexao.commit()
        print("Tabela 'usuarios' criada ou já existe.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar tabela usuarios: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def criar_tabela_contatos():
    conexao = conectar()
    if conexao is None:
        print("Erro ao conectar ao banco.")
        return

    cursor = None
    try:
        cursor = conexao.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS contatos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario_id INT,
                nome VARCHAR(255),
                telefone VARCHAR(20),
                email VARCHAR(255),
                perfil_rede_social VARCHAR(255),
                notas TEXT,
                data_nascimento DATE,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
        """
        cursor.execute(sql)
        conexao.commit()
        print("Tabela 'contatos' criada ou já existe.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar tabela contatos: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def salvar_usuario(nome, email, contato, senha, foto=None):
    conexao = conectar()
    if conexao is None:
        return False

    cursor = None
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
        if cursor.fetchone():
            return False

        sql = "INSERT INTO usuarios (nome, email, contato, senha_hash, foto) VALUES (%s, %s, %s, SHA2(%s, 256), %s)"
        valores = (nome, email, contato, senha, foto)
        cursor.execute(sql, valores)
        conexao.commit()
        return True
    except mysql.connector.Error as e:
        print(f"Erro ao salvar usuario: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def autenticar_usuario(email, senha):
    conexao = conectar()
    if conexao is None:
        return False, None, None, None

    cursor = None
    try:
        cursor = conexao.cursor()
        sql = "SELECT id, nome, foto FROM usuarios WHERE email = %s AND senha_hash = SHA2(%s, 256)"
        cursor.execute(sql, (email, senha))
        usuario = cursor.fetchone()
        if usuario:
            return True, usuario[0], usuario[1], usuario[2]  # id, nome, foto
        return False, None, None, None
    except mysql.connector.Error as e:
        print(f"Erro ao autenticar usuario: {e}")
        return False, None, None, None
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def obter_foto_usuario(usuario_id):
    conexao = conectar()
    if conexao is None:
        return None

    cursor = None
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT foto FROM usuarios WHERE id = %s", (usuario_id,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None
    except mysql.connector.Error as e:
        print(f"Erro ao obter foto: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def salvar_contato(nome, email, telefone, data_nascimento, perfil_rede_social, notas, usuario_id):
    conexao = conectar()
    if conexao is None:
        return False

    cursor = None
    try:
        cursor = conexao.cursor()
        sql = """INSERT INTO contatos (nome, email, telefone, data_nascimento, perfil_rede_social, notas, usuario_id)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        valores = (nome, email, telefone, data_nascimento, perfil_rede_social, notas, usuario_id)
        cursor.execute(sql, valores)
        conexao.commit()
        return True
    except mysql.connector.Error as e:
        print(f"Erro ao salvar contato: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def obter_contatos(usuario_id):
    conexao = conectar()
    if conexao is None:
        return []

    cursor = None
    try:
        cursor = conexao.cursor(dictionary=True)
        sql = """
            SELECT 
                id,
                nome, 
                IFNULL(telefone, '') AS telefone,
                email, 
                perfil_rede_social, 
                notas,
                data_nascimento
            FROM contatos 
            WHERE usuario_id = %s
        """
        cursor.execute(sql, (usuario_id,))
        contatos = cursor.fetchall()
        return contatos
    except mysql.connector.Error as e:
        print(f"Erro ao obter contatos: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def atualizar_contato(contato_id, nome, email, telefone, data_nascimento, perfil_rede_social, notas):
    conexao = conectar()
    if conexao is None:
        return False

    cursor = None
    try:
        cursor = conexao.cursor()
        sql = """
            UPDATE contatos 
            SET nome=%s, email=%s, telefone=%s, data_nascimento=%s, perfil_rede_social=%s, notas=%s 
            WHERE id=%s
        """
        valores = (nome, email, telefone, data_nascimento, perfil_rede_social, notas, contato_id)
        cursor.execute(sql, valores)
        conexao.commit()
        return True
    except mysql.connector.Error as e:
        print(f"Erro ao atualizar contato: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def deletar_contato(contato_id):
    conexao = conectar()
    if conexao is None:
        return False

    cursor = None
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM contatos WHERE id = %s"
        cursor.execute(sql, (contato_id,))
        conexao.commit()
        return True
    except mysql.connector.Error as e:
        print(f"Erro ao deletar contato: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def atualizar_foto_usuario(usuario_id, foto_data):
    try:
        conn = sqlite3.connect('contatos.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET foto = ? WHERE id = ?", (foto_data, usuario_id))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Erro ao atualizar foto: {e}")
        return False
    finally:
        conn.close()

# Criar tabelas ao iniciar
if __name__ == "__main__":
    criar_tabela_usuarios()
    criar_tabela_contatos()