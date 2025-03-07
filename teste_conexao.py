from bancodedados import conectar  # Importando a função do seu código

conexao = conectar()
if conexao:
    print("✅ Conexão estabelecida com sucesso!")
    conexao.close()  # Fecha a conexão após o teste
else:
    print("❌ Falha ao conectar ao banco de dados!")
