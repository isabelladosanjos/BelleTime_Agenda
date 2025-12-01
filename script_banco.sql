-- =======================================================================
-- SCRIPT DE CRIAÇÃO DO BANCO DE DADOS - PROJETO BELLE TIME
-- =======================================================================

-- 1. Criação e Seleção do Banco de Dados
CREATE DATABASE IF NOT EXISTS belletime_agendadb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE belletime_agendadb;

-- =======================================================================
-- 2. DDL - CRIAÇÃO DAS TABELAS (ESTRUTURA)
-- =======================================================================

-- Tabela de Segurança (Login)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(50) NOT NULL
);

-- Tabela de Clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    anotacoes TEXT
);

-- Tabela de Serviços (Cardápio)
CREATE TABLE IF NOT EXISTS servicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    duracao_minutos INT NOT NULL,
    preco DECIMAL(10, 2) NOT NULL
);

-- Tabela de Agendamentos (Principal)
CREATE TABLE IF NOT EXISTS agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    servico_id INT NOT NULL,
    data_hora DATETIME NOT NULL,
    status VARCHAR(20) DEFAULT 'Agendado',
    
    -- Chaves Estrangeiras (Relacionamentos)
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (servico_id) REFERENCES servicos(id)
);

-- =======================================================================
-- 3. DCL - CONFIGURAÇÃO DE USUÁRIO E PERMISSÕES
-- =======================================================================

-- Cria o usuário da aplicação (se não existir)
-- ATENÇÃO: Se for rodar em produção, mude a senha aqui!
CREATE USER IF NOT EXISTS 'isabella'@'%' IDENTIFIED BY '745181';

-- Garante as permissões apenas neste banco
GRANT ALL PRIVILEGES ON belletime_agendadb.* TO 'isabella'@'%';
FLUSH PRIVILEGES;

-- =======================================================================
-- 4. DML - INSERÇÃO DE DADOS INICIAIS (POPULAR O BANCO)
-- =======================================================================

-- 4.1. Usuário Administrador Padrão
-- Limpa usuário admin antigo para evitar erros e insere o novo
DELETE FROM usuarios WHERE login = 'admin';
INSERT INTO usuarios (login, senha) VALUES ('admin', 'admin');

-- 4.2. Clientes de Exemplo
INSERT INTO clientes (nome, telefone, anotacoes) VALUES
('Ana Costa', '(15) 99111-1111', 'Cliente teste'),
('Beatriz Lima', '(15) 99222-2222', 'Cliente VIP');

-- 4.3. Cardápio Completo de Serviços
-- (Valores iniciais definidos como 0.00 para serem ajustados no sistema)
INSERT INTO servicos (nome, duracao_minutos, preco) VALUES
('Avaliação Capilar', 30, 0.00),
('Coconut', 60, 0.00),
('Coloração total', 120, 0.00),
('Corte', 60, 0.00),
('Corte Bordado', 60, 0.00),
('Corte infantil', 45, 0.00),
('Cronograma Orgânico', 60, 0.00),
('Escova', 45, 0.00),
('Escova + prancha', 60, 0.00),
('Lavagem', 20, 0.00),
('Lavagem Terapêutica', 40, 0.00),
('Mechas inversas', 180, 0.00),
('Mechas', 180, 0.00),
('Progressiva', 180, 0.00),
('Retoque de raiz Coloração', 90, 0.00),
('Selagem', 120, 0.00),
('Terapia Capilar + Cronograma', 90, 0.00),
('Terapia Capilar personalizada', 90, 0.00),
('Teste de Mechas', 30, 0.00),
('Tonalização', 60, 0.00),
('Tratamento (hidratação, nutrição, reconstrução)', 60, 0.00),
('Tratamento pediculose', 60, 0.00);