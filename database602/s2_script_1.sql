-- Active: 1730647917074@@127.0.0.1@3307
-- script corre completamente no SQL Server Manager
-- comandos TOP and LEN não correm diretamente aqui

DROP DATABASE IF EXISTS uc606;
GO

CREATE DATABASE uc606;
GO
USE uc606;
GO

create table tab_A(
id int primary key,
nome varchar(100)
);
go

INSERT INTO tab_A (id, nome)
VALUES
(1, 'ANA'), (2, 'RICARDO'), (3, 'JOÃO');

select * from tab_A;

select * from tab_A
order by 1;

select * from tab_A
order by 2, 1;

select * from tab_A
where nome <> 'RICARDO';

select * from tab_A
where id > 1;

select * from tab_A
where id >= 1;

select * from tab_A
where id between 1 and 3; -- between n�o conta s� o intervalo

select * from tab_A
where id is null;

select top (2) * from tab_A;

select lower(nome) from tab_A;

select len(nome) from tab_A;

select top (2) id, lower(nome) as nome_maiusculo 
from tab_A
order by nome;

select nome, len(nome) as qtd_caracteres 
from tab_A
order by len(nome);

select nome, reverse(nome) as nome_invertido 
from tab_A
order by nome;

select nome, reverse(nome) as nome_invertido 
from tab_A
order by len(nome) desc;

select getdate() as hoje, 
dateadd(month, 3, getdate()) as futura_consulta;

-- as funções top e len não funcionam
-- correm apenas no sql server manager studio