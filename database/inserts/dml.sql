-- Inserindo valores ta tabela clientes
INSERT INTO clientes(nome, telefone, cpf) VALUES
('Elizabeth Maria', '8699874-5678', '12345678900'),
('Rian Michel', '8698765-0098', '87512345678'),
('Alex Henrique', '8691234-8754', '54321098761'),
('Maria Geisilane', '8695656-0987', '88855544412'),
('Carlos Henrique', '8694432-0912', '11122233345');

-- Inserindo valores na tabela bicicletas
INSERT INTO bicicletas(modelo, status, preco_hora) VALUES
('Caloi 10', 'disponivel', 6.00),
('Monark', 'disponivel', 4.50),
('BMX', 'disponivel', 8.00);

-- Inserindo valores na tabela alugueis
INSERT INTO alugueis (fk_cliente, fk_bicicleta, data_aluguel, data_devolucao, horas_previstas) VALUES
(1, 1, '2026-04-20 10:00:00', '2026-04-20 12:00:00', 2),
(2, 2, '2026-04-21 14:00:00', '2026-04-21 16:00:00', 2),
(4, 3, '2026-04-22 16:50:12', '2026-04-23 13:09:15', 20);