-- Criando Procedure devolver_bicicleta para garantir que o aluguel existe e a bicicleta ainda não foi devolvida
CREATE OR REPLACE PROCEDURE devolver_bicicleta(p_id_aluguel INTEGER)
LANGUAGE plpgsql
AS $$
DECLARE
    v_id_bicicleta INTEGER;
    v_status VARCHAR(20);
BEGIN
		-- 1 - busca a bicicleta desse aluguel
	    SELECT fk_bicicleta
	    INTO v_id_bicicleta
	    FROM alugueis
	    WHERE id_aluguel = p_id_aluguel;
	
	    IF v_id_bicicleta IS NULL THEN
	        RAISE EXCEPTION 'Aluguel não encontrado';
	    END IF;

		-- 2 - verifica se essa bicicleta já não foi devolvida antes
	    SELECT status
	    INTO v_status
	    FROM bicicletas
	    WHERE id_bicicleta = v_id_bicicleta;
	
	    IF v_status = 'disponivel' THEN
	        RAISE EXCEPTION 'Esse aluguel já foi devolvido';
	    END IF;

		-- 3 - atualiza a data de devolução do aluguel
	    UPDATE alugueis
	    SET data_devolucao = NOW()
	    WHERE id_aluguel = p_id_aluguel;

		-- 4 - libera a bicicleta
	    UPDATE bicicletas
	    SET status = 'disponivel'
	    WHERE id_bicicleta = v_id_bicicleta;
END;
$$;

-- Devolvendo a bicicleta id 1
CALL devolver_bicicleta(1);

-- Verificando se a Procedure funcionou
SELECT * FROM alugueis;

SELECT * FROM bicicletas;

-- Testando se colocar novamente uma bicicleta já devolvida trás mensagem de erro
CALL devolver_bicicleta(1);

-- Testando se colocar id inexistente aparece mensagem de erro
CALL devolver_bicicleta(9999);