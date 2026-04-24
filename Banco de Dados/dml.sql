--- INSERÇÃO CLIENTES
INSERT INTO clientes(nome, telefone, cpf) VALUES
('Elizabeth Maria', '8699874-5678', '12345678900'),
('Rian Michel', '8698765-0098', '87512345678'),
('Alex Henrique', '8691234-8754', '54321098761'),
('Maria Geisilane', '8695656-0987', '88855544412'),
('Carlos Henrique', '8694432-0912', '11122233345');

--- INSERÇÃO BICICLETAS
INSERT INTO bicicletas(modelo, status) VALUES
('Caloi 10', 'disponivel'),
('Monark', 'disponivel'),
('BMX', 'disponivel');

--- INSERÇÃO ALUGUEIS
INSERT INTO alugueis (fk_cliente, fk_bicicleta, data_aluguel, data_devolucao) VALUES
(1, 1, '2026-04-20 10:00:00', '2026-04-20 12:00:00'),
(2, 2, '2026-04-21 14:00:00', '2026-04-21 16:00:00'),
(4, 3, '2026-04-22 16:50:12', '2026-04-23 13:09:15');

--- ATUALIZAR TELEFONE CLIENTE 2
UPDATE clientes
SET telefone = '8696666-6666'
WHERE id_cliente = 2;

--- ATUALIZAR STATUS DA BICICLETA 1
UPDATE bicicletas 
SET status = 'alugada'
WHERE id_bicicleta = 1;

--- ATUALIZAR DATA DE DEVOLUCAO DO CLIENTE 4
UPDATE alugueis
SET data_devolucao = '2026-04-25 13:00:00'
WHERE fk_cliente = 4;

--- DELETAR CLIENTE
DELETE FROM clientes
WHERE id_cliente = 3;