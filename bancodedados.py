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
            return True, usuario[0], usuario[1]  # Retorna True e o nome do usuário
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

def salvar_contato(nome, email, telefone, data_nascimento, perfil_rede_social, notas, usuario_id):
    """Salva um novo contato no banco de dados vinculado a um usuário."""
    conexao = conectar()
    if conexao is None:
        print("⚠ Erro na conexão com o banco de dados.")
        return False

    cursor = None
    try:
        cursor = conexao.cursor()

        # 🔍 Verifica os dados antes de inserir
        print(f"📩 Tentando salvar: Nome={nome}, Telefone={telefone}, Data={data_nascimento}")

        sql = """INSERT INTO contatos (nome, email, telefone, data_nascimento, perfil_rede_social, notas, usuario_id)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        valores = (nome, email, telefone, data_nascimento, perfil_rede_social, notas, usuario_id)

        print(f"📝 Query SQL: {sql}")
        print(f"📊 Valores a serem inseridos: {valores}")  # 🔥 Veja se o telefone está aqui corretamente!

        cursor.execute(sql, valores)
        conexao.commit()

        print("✅ Contato salvo com sucesso!")
        return True
    except mysql.connector.Error as e:
        print(f"❌ Erro ao salvar contato: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()



def obter_contatos(usuario_id):
    """Retorna apenas os contatos do usuário logado."""
    conexao = conectar()
    if conexao is None:
        return []

    cursor = conexao.cursor(dictionary=True)

    # 🔥 Ajustando a consulta para garantir que a chave no dicionário tenha o nome correto
    sql = """
        SELECT 
            nome, 
            IFNULL(telefone, '') AS telefone,  -- ✅ Se for NULL, substitui por string vazia
            email, 
            perfil_rede_social, 
            notas 
        FROM contatos 
        WHERE usuario_id = %s
    """
    cursor.execute(sql, (usuario_id,))
    contatos = cursor.fetchall()

    cursor.close()
    conexao.close()

    print(f"📋 Contatos carregados: {contatos}")  # 🔥 Debug para verificar os dados retornados

    return contatos  # Retorna os contatos do usuário autenticado


    

