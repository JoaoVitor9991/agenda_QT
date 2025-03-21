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
                nome VARCHAR(255),
                email VARCHAR(255),
                telefone VARCHAR(20),
                data_nascimento DATE,
                perfil_rede_social VARCHAR(255),
                notas TEXT,
                usuario_id INT,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
        """
        cursor.execute(sql)
        conexao.commit()
        print("Tabela 'contatos' criada ou já existe.")
    except mysql.connector.Error as e:
        print(f"Erro ao criar tabela: {e}")
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

def verificar_contatos(usuario_id):
    conexao = conectar()
    if conexao is None:
        print("Erro ao conectar ao banco.")
        return

    cursor = None
    try:
        cursor = conexao.cursor(dictionary=True)
        sql = """
            SELECT nome, data_nascimento 
            FROM contatos 
            WHERE usuario_id = %s
        """
        cursor.execute(sql, (usuario_id,))
        contatos = cursor.fetchall()
        if contatos:
            print(f"Contatos do usuário {usuario_id}:")
            for contato in contatos:
                nome = contato['nome']
                data = contato['data_nascimento']
                print(f"Nome: {nome}, Data de Nascimento: {data}")
        else:
            print("Nenhum contato encontrado.")
    except mysql.connector.Error as e:
        print(f"Erro ao verificar contatos: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

if __name__ == "__main__":
    # Criar a tabela (se ainda não existir)
    criar_tabela_contatos()

    # Salvar um contato de teste
    sucesso = salvar_contato(
        nome="Maria Teste",
        email="maria@teste.com",
        telefone="(11) 91234-5678",
        data_nascimento="1995-05-15",  # Formato YYYY-MM-DD
        perfil_rede_social="@maria",
        notas="Teste de data",
        usuario_id=1
    )
    if sucesso:
        print("Contato salvo com sucesso!")
    else:
        print("Erro ao salvar contato.")

    # Verificar os contatos salvos
    verificar_contatos(1)