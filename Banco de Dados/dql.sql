--- LISTANDO BICICLETAS DISPONIVEIS
SELECT * FROM bicicletas
WHERE status = 'disponivel';

--- BUSCANDO ALUGUEL DE CLIENTE ESPECÍFICO
SELECT clientes.nome, bicicletas.modelo, alugueis.data_aluguel
FROM alugueis
INNER JOIN clientes ON alugueis.fk_cliente = clientes.id_cliente
INNER JOIN bicicletas ON alugueis.fk_bicicleta = bicicletas.id_bicicleta
WHERE clientes.nome = 'Elizabeth Maria';

--- LISTANDO OS ALUGUEIS MAIS RECENTES
SELECT * FROM alugueis
ORDER BY data_aluguel DESC;

--- ORDENANDO CLIENTES EM ORDEM ALFABÉTICA
SELECT * FROM clientes
ORDER BY nome ASC;

--- LISTAR QUEM ALUGOU QUAL BICICLETA
SELECT clientes.nome, bicicletas.modelo, alugueis.data_aluguel, alugueis.data_devolucao
FROM alugueis
INNER JOIN clientes ON alugueis.fk_cliente = clientes.id_cliente
INNER JOIN bicicletas ON alugueis.fk_bicicleta = bicicletas.id_bicicleta;

--- LISTAS TODOS OS CLIENTES (MESMO SEM ALUGUEL)
SELECT clientes.nome, alugueis.id_aluguel
FROM clientes
LEFT JOIN alugueis ON clientes.id_cliente = alugueis.fk_cliente;

---CONSULTA COMPLETA (CLIENTE, BICICLETA E DATA ALUGUEL)
SELECT clientes.nome AS cliente, bicicletas.modelo AS bicicleta, alugueis.data_aluguel AS data_de_aluguel
FROM alugueis
INNER JOIN clientes ON alugueis.fk_cliente = clientes.id_cliente
INNER JOIN bicicletas ON alugueis.fk_bicicleta = bicicletas.id_bicicleta
WHERE bicicletas.status = 'disponivel'
ORDER BY alugueis.data_aluguel DESC;