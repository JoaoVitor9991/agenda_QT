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
    """Verifica se o usuário existe e se a senha está correta no banco de dados."""
    conexao = conectar()
    if conexao is None:
        print("⚠ Erro na conexão com o banco de dados.")
        return False, None

    cursor = None
    try:
        cursor = conexao.cursor()

        # Consulta para verificar se o usuário existe e se a senha está correta
        sql = "SELECT id, nome FROM usuarios WHERE email = %s AND senha_hash = SHA2(%s, 256)"
        cursor.execute(sql, (email, senha))
        usuario = cursor.fetchone()

        if usuario:
            print(f"✅ Usuário autenticado: {usuario[1]}")
            return True, usuario[1]  # Retorna True e o nome do usuário
        else:
            print("❌ Email ou senha incorretos.")
            return False, None
    except mysql.connector.Error as e:
        print(f"❌ Erro ao autenticar usuário: {e}")
        return False, None
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

