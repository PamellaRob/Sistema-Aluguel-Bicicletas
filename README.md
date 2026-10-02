# 🚲 Sistema de Aluguel de Bicicletas

Sistema para controle de aluguel de bicicletas, com cadastro de
clientes, controle de bicicletas disponíveis/alugadas, registro de
aluguéis, devoluções e relatórios.

Este trabalho evolui o CRUD desenvolvido anteriormente, acrescentando
uma **View**, uma **Function** e uma **Procedure** integradas
diretamente às funcionalidades da aplicação.

## Identificação
- **Nome:** Pamella Roberta dos Santos Silva
- **Disciplina:** Projeto de Banco de Dados
- **Professor:** Anderson Soares Costa

## Sobre o projeto
O sistema permite cadastrar clientes, controlar o status das
bicicletas (disponível/alugada), registrar aluguéis e devoluções, e
consultar relatórios sobre o histórico de uso.

## Tecnologias utilizadas
- Python 3
- Tkinter (interface gráfica)
- psycopg2
- PostgreSQL

## Banco de dados
- **SGBD:** PostgreSQL
- **Tabelas principais:** `clientes`, `bicicletas` (com `preco_hora`), `alugueis` (com `horas_previstas`)

### Diagrama Entidade-Relacionamento
![Diagrama do banco](docs/DER%20Sistema%20Aluguel%20de%20Bicicleta%20atualizado.png)

### View — `vw_relatorio_alugueis`
Consolida cliente, bicicleta, preço/hora e valor do aluguel numa
única consulta. Usada na tela **Relatório Completo**.

### Function — `fn_calcular_valor_aluguel(id_aluguel)`
Calcula o valor cobrado em um aluguel (`horas_previstas × preco_hora`
da bicicleta). Usada dentro da View e na tela **Devolver Bicicleta**.

### Procedure — `devolver_bicicleta(id_aluguel)`
Processa a devolução de uma bicicleta: valida se o aluguel existe e
se já não foi devolvido, atualiza a data de devolução e libera a
bicicleta. Usada na tela **Devolver Bicicleta**.

## Estrutura do repositório
- `/src`
  - `main.py`
  - `interface.py`
- `/database`
  - `/tables` → `ddl.sql`
  - `/inserts` → `dml.sql`
  - `/views` → `vw_relatorio_alugueis.sql`
  - `/functions` → `fn_calcular_valor_aluguel.sql`
  - `/procedures` → `devolver_bicicleta.sql`
- `/docs`
  - `DER Sistema Aluguel de Bicicleta atualizado.png`


## Como executar
1. Crie o banco `SistemaAluguelDeBicicletas` no PostgreSQL.
2. Execute, nesta ordem, os scripts de `database/tables`,
   `database/inserts`, `database/views`, `database/functions` e
   `database/procedures`.
3. Instale as dependências: `pip install psycopg2-binary`.
4. Ajuste usuário/senha do banco em `src/main.py` e
   `src/interface.py`, se necessário.
5. Rode `python src/interface.py` (tela gráfica) ou
   `python src/main.py` (terminal). Login: `admin` / `1234`.

## Vídeo explicativo
🎥 [Clique para acessar o vídeo](https://drive.google.com/file/d/1UIx3DXbMWqK2EkLIgDlERAf-SMiJx29G/view?usp=drive_link)
