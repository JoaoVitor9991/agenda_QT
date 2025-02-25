CREATE DATABASE cadastro_cliente;
use cadastro_cliente;
create table cadastrar_cliente(
	CPF VARCHAR (11) PRIMARY KEY, 
    Nome VARCHAR(100) NOT NULL,
    RG VARCHAR (20),
    Fone VARCHAR(20),
    Id_cidade INT,
    Id_sexo INT,
    Id_raca int,
    ID_escolaridade INT,
    foreign key (Id_cidade) references cidade(Id_cidade),
    foreign key (Id_sexo) references sexo (Id_sexo),
    foreign key (Id_raca) references raca (Id_raca),
    foreign key (Id_escolaridade) references escolaridade(Id_escolaridade)
    );
    
create table estado (
		Id_estado INT primary key auto_increment,
        Estado varchar(50) not null
        );

create table cidade (
		Id_cidade INT PRIMARY KEY auto_increment,
        Cidade VARCHAR(50) NOT NULL,
        Id_estado INT,
        FOREIGN KEY (Id_estado) references estado(Id_estado)
        );

create table sexo (
	Id_sexo INT primary KEY auto_increment,
    Sexo VARCHAR(10) not null
    );
    
create table raca (
	Id_raca int primary key auto_increment,
    raca VARCHAR (30) NOT NULL
    );
    
create table escolaridade (
	Id_escolaridade int primary key auto_increment,
    Escolaridade VARCHAR (50) not null
    );
