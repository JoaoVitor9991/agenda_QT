import mysql.connector

def conectar():
    """Estabelece a conexão com o banco de dados MySQL."""
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",  # Troque pelo usuário correto se necessário
            password="",  # Coloque a senha se houver
            database="agenda"
        )
        return conexao
    except mysql.connector.Error as e:
        print(f"❌ Erro ao conectar ao MySQL: {e}")
        return None

def salvar_usuario(nome, email, contato, senha):
    """Insere um novo usuário no banco de dados."""
    conexao = conectar()
    if conexao is None:
        print("⚠ Erro na conexão com o banco de dados.")
        return False

    cursor = None
    try:
        cursor = conexao.cursor()

        # Verifica se o email já está cadastrado antes de inserir
        cursor.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
        if cursor.fetchone():
            print("❌ Erro: Email já cadastrado!")
            return False

        sql = "INSERT INTO usuarios (nome, email, contato, senha_hash) VALUES (%s, %s, %s, SHA2(%s, 256))"
        valores = (nome, email, contato, senha)

        cursor.execute(sql, valores)
        conexao.commit()

        print("✅ Usuário cadastrado com sucesso!")
        return True
    except mysql.connector.IntegrityError:
        print("❌ Erro: Email já cadastrado!")
        return False
    except mysql.connector.Error as e:
        print(f"❌ Erro ao salvar usuário: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def autenticar_usuario(email, senha):
    """Verifica se o usuário existe e retorna o ID e nome."""
    conexao = conectar()
    if conexao is None:
        print("⚠ Erro na conexão com o banco de dados.")
        return False, None, None

    cursor = None
    try:
        cursor = conexao.cursor()

        # Consulta para verificar se o usuário existe e se a senha está correta
        sql = "SELECT id, nome FROM usuarios WHERE email = %s AND senha_hash = SHA2(%s, 256)"
        cursor.execute(sql, (email, senha))
        usuario = cursor.fetchone()

        if usuario:
            print(f"✅ Usuário autenticado: {usuario[1]}")
            return True, usuario[0], usuario[1]  # 🔹 Retorna True, usuario_id e nome_usuario
        else:
            print("❌ Email ou senha incorretos.")
            return False, None, None
    except mysql.connector.Error as e:
        print(f"❌ Erro ao autenticar usuário: {e}")
        return False, None, None
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def salvar_contato(usuario_id, nome, telefone, email, rede_social, data_nascimento):
    """Salva um novo contato no banco de dados vinculado ao usuário logado."""
    conexao = conectar()
    if conexao is None:
        print("⚠ Erro na conexão com o banco de dados.")
        return False

    cursor = None
    try:
        cursor = conexao.cursor()

        sql = """INSERT INTO contatos (usuario_id, nome, telefone, email, rede_social, data_nascimento) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (usuario_id, nome, telefone, email, rede_social, data_nascimento)

        cursor.execute(sql, valores)
        conexao.commit()

        print(f"✅ Contato '{nome}' salvo com sucesso para o usuário {usuario_id}!")
        return True
    except mysql.connector.Error as e:
        print(f"❌ Erro ao salvar contato: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

    

def buscar_contatos(usuario_id):
    """Retorna todos os contatos de um usuário específico."""
    conexao = conectar()
    if conexao is None:
        print("⚠ Erro na conexão com o banco de dados.")
        return []

    cursor = None
    try:
        cursor = conexao.cursor(dictionary=True)  # Retorna os resultados como dicionário

        sql = "SELECT id, nome, telefone, email, rede_social, data_nascimento FROM contatos WHERE usuario_id = %s"
        cursor.execute(sql, (usuario_id,))
        contatos = cursor.fetchall()

        return contatos  # Retorna uma lista de contatos
    except mysql.connector.Error as e:
        print(f"❌ Erro ao buscar contatos: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

