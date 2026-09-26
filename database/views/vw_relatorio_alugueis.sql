-- Criando uma View para relatório de alugueis
CREATE OR REPLACE VIEW vw_relatorio_alugueis AS
SELECT
    a.id_aluguel, c.id_cliente, c.nome AS cliente,
    c.cpf, b.id_bicicleta, b.modelo AS bicicleta,
    b.preco_hora, b.status AS status_bicicleta,
    a.data_aluguel,
    a.data_devolucao,
    a.horas_previstas,
    fn_calcular_valor_aluguel(a.id_aluguel) AS valor_aluguel
FROM alugueis a
INNER JOIN clientes c   ON a.fk_cliente = c.id_cliente
INNER JOIN bicicletas b ON a.fk_bicicleta = b.id_bicicleta;

-- Verficando a View criando e ordenando pela data de aluguel (decrescente)
SELECT * FROM vw_relatorio_alugueis 
ORDER BY data_aluguel DESC;	