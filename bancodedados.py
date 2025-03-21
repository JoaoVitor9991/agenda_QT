import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="agenda"
        )
        return conexao
    except mysql.connector.Error as e:
        return None

def salvar_usuario(nome, email, contato, senha):
    conexao = conectar()
    if conexao is None:
        return False

    cursor = None
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
        if cursor.fetchone():
            return False

        sql = "INSERT INTO usuarios (nome, email, contato, senha_hash) VALUES (%s, %s, %s, SHA2(%s, 256))"
        valores = (nome, email, contato, senha)
        cursor.execute(sql, valores)
        conexao.commit()
        return True
    except mysql.connector.IntegrityError:
        return False
    except mysql.connector.Error:
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def autenticar_usuario(email, senha):
    conexao = conectar()
    if conexao is None:
        return False, None, None

    cursor = None
    try:
        cursor = conexao.cursor()
        sql = "SELECT id, nome FROM usuarios WHERE email = %s AND senha_hash = SHA2(%s, 256)"
        cursor.execute(sql, (email, senha))
        usuario = cursor.fetchone()
        if usuario:
            return True, usuario[0], usuario[1]
        else:
            return False, None, None
    except mysql.connector.Error:
        return False, None, None
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
    except mysql.connector.Error:
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
    except mysql.connector.Error:
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

if __name__ == "__main__":
    sucesso = salvar_contato(
        nome="João Teste",
        email="joao@teste.com",
        telefone="(11) 98765-4321",
        data_nascimento="1990-01-01",
        perfil_rede_social="@joaoteste",
        notas="Teste",
        usuario_id=1
    )
    if sucesso:
        contatos = obter_contatos(1)
        for contato in contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")