CREATE DATABASE IF NOT EXISTS meu_sistema;
 
-- Usar o banco de dados
USE meu_sistema;
 
-- Criar a tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
 
-- Inserir um usuário de teste
INSERT INTO usuarios (username, password) VALUES 
('admin', '1234'); -- Lembre-se de usar hash de senha na aplicação real!
 
 
select * from usuarios
 
 
