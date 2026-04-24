import psycopg2

#Conexão do Banco de Dados
def conectar():
    return psycopg2.connect(
        host="localhost",
        database="SistemaAluguelDeBicicletas",
        user="postgres",
        password="root"  
    )


#Login Usuario
def login():
    print("===== LOGIN =====")
    user = input("Usuário: ")
    senha = input("Senha: ")

    if user == "admin" and senha == "1234":
        print("Login OK!\n")
        return True
    else:
        print("Erro no login\n")
        return False

# Opção cadastrar cliente novo  
def cadastrar_cliente():
    con = conectar()
    cur = con.cursor()

    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")

    cur.execute(
        "INSERT INTO clientes (nome, telefone, cpf) VALUES (%s, %s, %s)",
        (nome, telefone, cpf)
    )

    con.commit()
    con.close()
    print("Cliente cadastrado!\n")

# Opção listar clientes cadastrados
def listar_clientes():
    con = conectar()
    cur = con.cursor()

    cur.execute("SELECT * FROM clientes")

    for c in cur.fetchall():
        print(c)

    con.close()
    print()

# Opção atualizar cliente (nome)
def atualizar_cliente():
    con = conectar()
    cur = con.cursor()

    id_cliente = input("ID do cliente: ")
    novo_nome = input("Novo nome: ")

    cur.execute(
        "UPDATE clientes SET nome = %s WHERE id_cliente = %s",
        (novo_nome, id_cliente)
    )

    con.commit()
    con.close()
    print("Atualizado!\n")

# Opção excluir cliente
def excluir_cliente():
    con = conectar()
    cur = con.cursor()

    id_cliente = input("ID do cliente: ")

    cur.execute(
        "DELETE FROM clientes WHERE id_cliente = %s",
        (id_cliente,)
    )

    con.commit()
    con.close()
    print("Cliente excluído\n")

# Opção de ver bicicletas disponiveis
def bicicletas_disponiveis():
    con = conectar()
    cur = con.cursor()

    cur.execute("SELECT * FROM bicicletas WHERE status = 'disponivel'")

    for b in cur.fetchall():
        print(b)

    con.close()
    print()

# Opção de ver bicicletas alugadas
def bicicletas_alugadas():
    con = conectar()
    cur = con.cursor()

    cur.execute("SELECT * FROM bicicletas WHERE status = 'alugada'")

    for b in cur.fetchall():
        print(b)

    con.close()
    print()

# Opção de alugar bicicleta
def alugar_bicicleta():
    con = conectar()
    cur = con.cursor()

    cliente = input("ID do cliente: ")
    bike = input("ID da bicicleta: ")

    cur.execute("""
        INSERT INTO alugueis (fk_cliente, fk_bicicleta, data_aluguel, data_devolucao)
        VALUES (%s, %s, NOW(), NOW())
    """, (cliente, bike))

    cur.execute("UPDATE bicicletas SET status = 'alugada' WHERE id_bicicleta = %s", (bike,))

    con.commit()
    con.close()
    print("Aluguel realizado!\n")

#Opção de devolver bicicleta já alugada
def devolver_bicicleta():
    con = conectar()
    cur = con.cursor()

    id_aluguel = input("ID do aluguel: ")

    # atualizar data de devolução
    cur.execute("""
        UPDATE alugueis
        SET data_devolucao = NOW()
        WHERE id_aluguel = %s
    """, (id_aluguel,))

    # pegar id da bicicleta desse aluguel
    cur.execute("""
        SELECT fk_bicicleta
        FROM alugueis
        WHERE id_aluguel = %s
    """, (id_aluguel,))

    resultado = cur.fetchone()

    if resultado:
        id_bike = resultado[0]

        # atualizar status da bicicleta
        cur.execute("""
            UPDATE bicicletas
            SET status = 'disponivel'
            WHERE id_bicicleta = %s
        """, (id_bike,))

        con.commit()
        print("Bicicleta devolvida com sucesso!\n")
    else:
        print("Aluguel não encontrado!\n")

    con.close()

# Opção de ver relatório completo dos clientes com alugueis(data de aluguel e data de devolução)
def relatorio_completo():
    con = conectar()
    cur = con.cursor()

    cur.execute("""
        SELECT c.nome, b.modelo, a.data_aluguel, a.data_devolucao
        FROM alugueis a
        INNER JOIN clientes c ON a.fk_cliente = c.id_cliente
        INNER JOIN bicicletas b ON a.fk_bicicleta = b.id_bicicleta
    """)

    print("\n===== RELATÓRIO COMPLETO =====")
    for r in cur.fetchall():
        print(r)

    con.close()
    print()

# Opção de ver clientes que alugaram bicicletas 
def clientes_com_aluguel():
    con = conectar()
    cur = con.cursor()

    cur.execute("""
        SELECT DISTINCT c.nome
        FROM clientes c
        INNER JOIN alugueis a ON c.id_cliente = a.fk_cliente
    """)

    print("\n===== CLIENTES COM ALUGUEL =====")
    for r in cur.fetchall():
        print(r)

    con.close()
    print()

# Opção de ver clientes que não alugaram bicicletas
def clientes_sem_aluguel():
    con = conectar()
    cur = con.cursor()

    cur.execute("""
        SELECT c.nome
        FROM clientes c
        LEFT JOIN alugueis a ON c.id_cliente = a.fk_cliente
        WHERE a.id_aluguel IS NULL
    """)

    print("\n===== CLIENTES SEM ALUGUEL =====")
    for r in cur.fetchall():
        print(r)

    con.close()
    print()


# Menu principal
def menu():
    while True:
        print("===== MENU =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("5 - Ver bicicletas disponíveis")
        print("6 - Ver bicicletas alugadas")
        print("7 - Alugar bicicleta")
        print("8 - Devolver bicicleta")
        print("9- Relatório completo de alugueis")
        print("10- Clientes com aluguel")
        print("11- Clientes sem aluguel")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1": cadastrar_cliente()
        elif op == "2": listar_clientes()
        elif op == "3": atualizar_cliente()
        elif op == "4": excluir_cliente()
        elif op == "5": bicicletas_disponiveis()
        elif op == "6": bicicletas_alugadas()
        elif op == "7": alugar_bicicleta()
        elif op == "8": devolver_bicicleta()
        elif op == "9": relatorio_completo()
        elif op == "10": clientes_com_aluguel()
        elif op == "11": clientes_sem_aluguel()
        elif op == "0": break
        else: print("Opção inválida! Tente novamente\n")


if __name__ == "__main__":
    if login():
        menu()