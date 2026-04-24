# 🚲 Sistema de Aluguel de Bicicletas

Este projeto foi desenvolvido como trabalho prático da disciplina de Banco de Dados. O objetivo é demonstrar a integração de uma aplicação em Python com um banco de dados relacional PostgreSQL, realizando operações de CRUD e consultas com JOIN.

---

## 📌 Sobre o Projeto

O sistema simula o funcionamento de uma locadora de bicicletas, permitindo:

- Cadastro de clientes
- Visualização de bicicletas disponíveis e alugadas
- Realização de aluguéis
- Devolução de bicicletas
- Relatórios com consultas SQL (INNER JOIN e LEFT JOIN)

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.14.4
- **Banco de Dados:** PostgreSQL
- **Biblioteca de conexão:** `psycopg2`
- **Interface:** Tkinter (Interface gráfica) + Terminal

---

## 📂 Estrutura do Repositório

* `/diagrama`: Diagrama Entidade-Relacionamento (DER).
* `/ddl`: Scripts de criação (CREATE TABLE, Constraints).
* `/dml`: Scripts de manipulação (INSERT, UPDATE, DELETE).
* `/dql`: Scripts de consulta (SELECT, JOINs, Filtros).
* `/projeto sistema aluguel de bicicletas`: Código-fonte da aplicação (Python).

---

## 📸 Demonstração (Prints do Sistema)

### 🔐 Tela de Login
<img width="370" height="313" alt="Captura de tela 2026-04-23 232428" src="https://github.com/user-attachments/assets/d844f1c3-724b-4802-a09b-ea9110433a7c" />

---

### 📋 Menu Principal
<img width="475" height="919" alt="Captura de tela 2026-04-23 232456" src="https://github.com/user-attachments/assets/93870f31-8d2d-4437-8bfb-427ef5d4ac59" />


---

### 🔗 Consulta com JOIN (Relatório Completo)
<img width="768" height="509" alt="Captura de tela 2026-04-23 232607" src="https://github.com/user-attachments/assets/0f25d700-6588-45cb-ae86-5ae0bb01848f" />


---

## 📺 Vídeo Demonstrativo

Confira a explicação completa do sistema no link abaixo:

👉 COLOQUE_AQUI_O_LINK_DO_VIDEO

---

## 🚀 Como Executar o Projeto

### Configurar o Banco de Dados

1. Crie um banco no PostgreSQL: SistemaAluguelDeBicicletas

2. Execute o script da pasta `/ddl` para criar as tabelas.

3. (Opcional) Execute os scripts da pasta `/dml` para inserir dados.

---

### Executar o Sistema

1. Abra o projeto no VS Code

2. Crie e ative o ambiente virtual: `python -m venv .venv .venv\Scripts\activate`

3. Instale a dependência: `pip install psycopg2-binary`

4. Execute o sistema: `python main.py` ou `python interface.py`

---

## 📄 Regras de Negócio e Consultas

O sistema implementa consultas SQL com diferentes níveis de complexidade:

### 🔗 INNER JOIN
Utilizado para exibir apenas clientes que alugaram bicicletas:

```sql
SELECT DISTINCT c.nome
        FROM clientes c
        INNER JOIN alugueis a ON c.id_cliente = a.fk_cliente
```

### 🔗 LEFT JOIN
Utilizado para exibir clientes que NÃO alugaram bicicletas:

```sql
SELECT c.nome
        FROM clientes c
        LEFT JOIN alugueis a ON c.id_cliente = a.fk_cliente
        WHERE a.id_aluguel IS NULL
```

---

### 👤 Autor

* **Pamella Roberta dos Santos Silva** - [robertapamella422@gmail.com](mailto:robertapamella422@gmail.com)
