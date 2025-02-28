import mysql.connector
 
def conectar():
    return mysql.connector.connect(
      host="localhost",
      user="seu_usuario",
      password="sua_senha",
      database="seu_banco_de_dados"
  )
 
def adicionar_user(login, senha):
    conexao= conectar()
    cursor= conexao.cursor ()
    sql = "INSERT INTO usuarios (email, senha_hash) VALUES (%s, SHA2(%s, 256))"
    valores = (login, senha)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()