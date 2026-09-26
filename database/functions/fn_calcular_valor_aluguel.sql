-- Criando Function para retornar quanto deu o aluguel da bicicleta (Horas alugadas * Preço/Hora da bicicleta)
CREATE OR REPLACE FUNCTION fn_calcular_valor_aluguel(p_id_aluguel INTEGER)
RETURNS NUMERIC
AS $$
DECLARE
    v_horas NUMERIC;
    v_preco_hora NUMERIC;
    v_valor NUMERIC;
BEGIN
	    SELECT a.horas_previstas, b.preco_hora
	    INTO v_horas, v_preco_hora
	    FROM alugueis a
	    INNER JOIN bicicletas b ON a.fk_bicicleta = b.id_bicicleta
	    WHERE a.id_aluguel = p_id_aluguel;
	
	    IF v_horas < 1 THEN
	        v_horas := 1;
	    END IF;
	
	    v_valor := v_horas * v_preco_hora;
	
	    RETURN v_valor;
END;
$$ LANGUAGE plpgsql;


-- Verificando a function criada e o valor do aluguel do id 1
SELECT fn_calcular_valor_aluguel(1);