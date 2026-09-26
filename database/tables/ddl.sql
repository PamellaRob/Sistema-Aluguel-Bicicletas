-- Criando tabela clientes
CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    telefone VARCHAR(20),
    cpf VARCHAR(11) UNIQUE NOT NULL,
    CHECK (char_length(cpf) = 11)
);
-- Criando tabela bicicleta com a nova coluna (preco_hora)
CREATE TABLE bicicletas (
    id_bicicleta SERIAL PRIMARY KEY,
    modelo VARCHAR(150) NOT NULL,
    status VARCHAR(20) NOT NULL,
    preco_hora NUMERIC(10,2) NOT NULL DEFAULT 5.00
);

-- Criando tabela alugueis com a nova coluna (horas_previstas)
CREATE TABLE alugueis (
    id_aluguel SERIAL PRIMARY KEY,
    fk_cliente INT NOT NULL,
    fk_bicicleta INT NOT NULL,
    data_aluguel TIMESTAMP NOT NULL,
    data_devolucao TIMESTAMP NOT NULL,
    horas_previstas NUMERIC(5,2) NOT NULL DEFAULT 1,
    FOREIGN KEY (fk_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (fk_bicicleta) REFERENCES bicicletas(id_bicicleta)
);