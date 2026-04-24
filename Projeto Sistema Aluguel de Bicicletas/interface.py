import tkinter as tk
from tkinter import messagebox, ttk
import psycopg2

#Conexão do Banco de Dados
def conectar():
    return psycopg2.connect(
        host="localhost",
        database="SistemaAluguelDeBicicletas",
        user="postgres",
        password="root"
    )

# Tela de login
def tela_login():
    win = tk.Tk()
    win.title("Login")
    win.geometry("300x220")
    win.resizable(False, False)
    win.configure(bg="#f0f0f0")

    tk.Label(win, text="== SISTEMA DE BICICLETAS ==",
             font=("Arial", 11, "bold"), bg="#f0f0f0").pack(pady=18)

    tk.Label(win, text="Usuário:", bg="#f0f0f0").pack()
    e_user = tk.Entry(win, width=25)
    e_user.pack(pady=3)

    tk.Label(win, text="Senha:", bg="#f0f0f0").pack()
    e_senha = tk.Entry(win, width=25, show="*")
    e_senha.pack(pady=3)

    def fazer_login():
        if e_user.get() == "admin" and e_senha.get() == "1234":
            win.destroy()
            tela_menu()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
            e_senha.delete(0, "end")

    tk.Button(win, text="Entrar", width=15, bg="#4a90d9", fg="white",
              command=fazer_login).pack(pady=14)

    e_user.focus()
    win.bind("<Return>", lambda e: fazer_login())
    win.mainloop()


# Tela do menu principal
def tela_menu():
    win = tk.Tk()
    win.title("Sistema de Bicicletas")
    win.geometry("380x580")
    win.resizable(False, True)
    win.configure(bg="#f0f0f0")

    tk.Label(win, text="== SISTEMA DE BICICLETAS ==",
             font=("Arial", 13, "bold"), bg="#f0f0f0").pack(pady=16)

    def btn(texto, cmd, cor="#4a90d9"):
        tk.Button(win, text=texto, width=30, height=2,
                  bg=cor, fg="white", font=("Arial", 10),
                  command=cmd).pack(pady=4)

    #Clientes
    tk.Label(win, text="── CLIENTES ──", bg="#f0f0f0",
             font=("Arial", 9, "bold"), fg="#555").pack(pady=(8, 0))
    btn("Cadastrar Cliente",  lambda: abrir_cadastrar_cliente(win))
    btn("Listar Clientes",    lambda: abrir_listar_clientes(win))

    #Bicicletas
    tk.Label(win, text="── BICICLETAS ──", bg="#f0f0f0",
             font=("Arial", 9, "bold"), fg="#555").pack(pady=(8, 0))
    btn("Ver Disponíveis",    lambda: abrir_bikes(win, "disponivel"), cor="#27ae60")
    btn("Ver Alugadas",       lambda: abrir_bikes(win, "alugada"),    cor="#e67e22")

    #Aluguel
    tk.Label(win, text="── ALUGUEL ──", bg="#f0f0f0",
             font=("Arial", 9, "bold"), fg="#555").pack(pady=(8, 0))
    btn("Alugar Bicicleta",   lambda: abrir_alugar(win))
    btn("Devolver Bicicleta", lambda: abrir_devolver(win), cor="#8e44ad")

    #Relatorios
    tk.Label(win, text="── RELATÓRIOS ──", bg="#f0f0f0",
             font=("Arial", 9, "bold"), fg="#555").pack(pady=(8, 0))
    btn("Relatório Completo",    lambda: abrir_relatorio(win))
    btn("Clientes com Aluguel",  lambda: abrir_clientes_com(win))
    btn("Clientes sem Aluguel",  lambda: abrir_clientes_sem(win))
    btn("Histórico por Cliente", lambda: abrir_historico_cliente(win), cor="#16a085")

    win.mainloop()


#Função de cadastrar clientes
def abrir_cadastrar_cliente(pai):
    win = tk.Toplevel(pai)
    win.title("Cadastrar Cliente")
    win.geometry("320x240")
    win.resizable(False, False)
    win.configure(bg="#f0f0f0")
    win.grab_set()

    tk.Label(win, text="Cadastrar Cliente",
             font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=12)

    tk.Label(win, text="Nome:", bg="#f0f0f0").pack()
    e_nome = tk.Entry(win, width=30); e_nome.pack(pady=3)

    tk.Label(win, text="Telefone:", bg="#f0f0f0").pack()
    e_tel = tk.Entry(win, width=30); e_tel.pack(pady=3)

    tk.Label(win, text="CPF:", bg="#f0f0f0").pack()
    e_cpf = tk.Entry(win, width=30); e_cpf.pack(pady=3)

    def salvar():
        nome = e_nome.get().strip()
        tel  = e_tel.get().strip()
        cpf  = e_cpf.get().strip()
        if not nome or not cpf:
            messagebox.showwarning("Atenção", "Nome e CPF são obrigatórios!", parent=win)
            return
        try:
            con = conectar(); cur = con.cursor()
            cur.execute("INSERT INTO clientes (nome, telefone, cpf) VALUES (%s,%s,%s)",
                        (nome, tel, cpf))
            con.commit(); con.close()
            messagebox.showinfo("OK", "Cliente cadastrado!", parent=win)
            e_nome.delete(0,"end"); e_tel.delete(0,"end"); e_cpf.delete(0,"end")
            e_nome.focus()
        except Exception as ex:
            messagebox.showerror("Erro", str(ex), parent=win)

    tk.Button(win, text="Salvar", width=20, bg="#4a90d9", fg="white",
              command=salvar).pack(pady=12)


#Função de listar clientes
def abrir_listar_clientes(pai):
    win = tk.Toplevel(pai)
    win.title("Clientes Cadastrados")
    win.geometry("560x400")
    win.configure(bg="#f0f0f0")
    win.grab_set()

    tk.Label(win, text="Clientes Cadastrados",
             font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)

    cols = ("ID", "Nome", "Telefone", "CPF")
    tree = ttk.Treeview(win, columns=cols, show="headings", height=12)
    for c, w in zip(cols, [50, 200, 130, 130]):
        tree.heading(c, text=c); tree.column(c, width=w, anchor="center")
    tree.pack(padx=12, pady=4, fill="both", expand=True)

    def carregar():
        tree.delete(*tree.get_children())
        try:
            con = conectar(); cur = con.cursor()
            cur.execute("SELECT id_cliente, nome, telefone, cpf FROM clientes")
            for r in cur.fetchall():
                tree.insert("", "end", values=r)
            con.close()
        except Exception as ex:
            messagebox.showerror("Erro", str(ex), parent=win)

    carregar()

    bar = tk.Frame(win, bg="#f0f0f0"); bar.pack(pady=8)

    def atualizar():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Atenção", "Selecione um cliente.", parent=win); return
        row = tree.item(sel[0])["values"]

        d = tk.Toplevel(win); d.title("Atualizar Nome"); d.geometry("300x140")
        d.resizable(False,False); d.configure(bg="#f0f0f0"); d.grab_set()
        tk.Label(d, text="Novo nome:", bg="#f0f0f0").pack(pady=10)
        e = tk.Entry(d, width=28); e.insert(0, row[1]); e.pack()
        def ok():
            try:
                con = conectar(); cur = con.cursor()
                cur.execute("UPDATE clientes SET nome=%s WHERE id_cliente=%s", (e.get().strip(), row[0]))
                con.commit(); con.close()
                messagebox.showinfo("OK","Nome atualizado!",parent=d)
                d.destroy(); carregar()
            except Exception as ex:
                messagebox.showerror("Erro",str(ex),parent=d)
        tk.Button(d, text="Salvar", bg="#4a90d9", fg="white", width=16, command=ok).pack(pady=10)

    def excluir():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Atenção", "Selecione um cliente.", parent=win); return
        row = tree.item(sel[0])["values"]
        if messagebox.askyesno("Confirmar", f"Excluir '{row[1]}'?", parent=win):
            try:
                con = conectar(); cur = con.cursor()
                cur.execute("DELETE FROM clientes WHERE id_cliente=%s", (row[0],))
                con.commit(); con.close()
                carregar()
            except Exception as ex:
                messagebox.showerror("Erro", str(ex), parent=win)

    tk.Button(bar, text="Atualizar Nome", bg="#4a90d9", fg="white",
              width=18, command=atualizar).pack(side="left", padx=6)
    tk.Button(bar, text="Excluir", bg="#e74c3c", fg="white",
              width=14, command=excluir).pack(side="left", padx=6)


#Função de ver bicicletas(disponíveis ou alugadas)
def abrir_bikes(pai, status):
    titulo = "Bicicletas Disponíveis" if status == "disponivel" else "Bicicletas Alugadas"
    win = tk.Toplevel(pai)
    win.title(titulo)
    win.geometry("500x360")
    win.configure(bg="#f0f0f0")
    win.grab_set()

    tk.Label(win, text=titulo, font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)

    try:
        con = conectar(); cur = con.cursor()
        cur.execute("SELECT * FROM bicicletas LIMIT 0")
        col_names = [d[0] for d in cur.description]
        con.close()
    except Exception as ex:
        messagebox.showerror("Erro", str(ex), parent=win); return

    tree = ttk.Treeview(win, columns=col_names, show="headings", height=13)
    col_w = max(70, 460 // len(col_names))
    for c in col_names:
        tree.heading(c, text=c.replace("_", " ").title())
        tree.column(c, width=col_w, anchor="center")
    tree.pack(padx=12, pady=4, fill="both", expand=True)

    try:
        con = conectar(); cur = con.cursor()
        cur.execute("SELECT * FROM bicicletas WHERE status = %s", (status,))
        for r in cur.fetchall():
            tree.insert("", "end", values=r)
        con.close()
    except Exception as ex:
        messagebox.showerror("Erro", str(ex), parent=win)


# Função de alugar bicicletas
def abrir_alugar(pai):
    win = tk.Toplevel(pai)
    win.title("Alugar Bicicleta")
    win.geometry("320x200")
    win.resizable(False, False)
    win.configure(bg="#f0f0f0")
    win.grab_set()

    tk.Label(win, text="Alugar Bicicleta",
             font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=12)

    tk.Label(win, text="ID do Cliente:", bg="#f0f0f0").pack()
    e_cli = tk.Entry(win, width=25); e_cli.pack(pady=3)

    tk.Label(win, text="ID da Bicicleta:", bg="#f0f0f0").pack()
    e_bike = tk.Entry(win, width=25); e_bike.pack(pady=3)

    def confirmar():
        cli  = e_cli.get().strip()
        bike = e_bike.get().strip()
        if not cli or not bike:
            messagebox.showwarning("Atenção", "Preencha os dois campos.", parent=win); return
        try:
            con = conectar(); cur = con.cursor()
            cur.execute("""
                INSERT INTO alugueis (fk_cliente, fk_bicicleta, data_aluguel, data_devolucao)
                VALUES (%s, %s, NOW(), NOW())
            """, (cli, bike))
            cur.execute("UPDATE bicicletas SET status='alugada' WHERE id_bicicleta=%s", (bike,))
            con.commit(); con.close()
            messagebox.showinfo("OK", "Aluguel realizado!", parent=win)
            win.destroy()
        except Exception as ex:
            messagebox.showerror("Erro", str(ex), parent=win)

    tk.Button(win, text="Confirmar Aluguel", width=22, bg="#27ae60", fg="white",
              command=confirmar).pack(pady=14)


# Função de devolver bicicletas
def abrir_devolver(pai):
    win = tk.Toplevel(pai)
    win.title("Devolver Bicicleta")
    win.geometry("300x160")
    win.resizable(False, False)
    win.configure(bg="#f0f0f0")
    win.grab_set()

    tk.Label(win, text="Devolver Bicicleta",
             font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=12)

    tk.Label(win, text="ID do Aluguel:", bg="#f0f0f0").pack()
    e_id = tk.Entry(win, width=25); e_id.pack(pady=3)

    def confirmar():
        id_al = e_id.get().strip()
        if not id_al:
            messagebox.showwarning("Atenção", "Informe o ID do aluguel.", parent=win); return
        try:
            con = conectar(); cur = con.cursor()
            cur.execute("UPDATE alugueis SET data_devolucao=NOW() WHERE id_aluguel=%s", (id_al,))
            cur.execute("SELECT fk_bicicleta FROM alugueis WHERE id_aluguel=%s", (id_al,))
            res = cur.fetchone()
            if res:
                cur.execute("UPDATE bicicletas SET status='disponivel' WHERE id_bicicleta=%s", (res[0],))
                con.commit(); con.close()
                messagebox.showinfo("OK", "Bicicleta devolvida!", parent=win)
                win.destroy()
            else:
                con.close()
                messagebox.showerror("Erro", "Aluguel não encontrado.", parent=win)
        except Exception as ex:
            messagebox.showerror("Erro", str(ex), parent=win)

    tk.Button(win, text="Confirmar Devolução", width=22, bg="#8e44ad", fg="white",
              command=confirmar).pack(pady=14)


# Opção de ver relatório completo dos clientes com alugueis(data de aluguel e data de devolução)
def abrir_relatorio(pai):
    win = tk.Toplevel(pai)
    win.title("Relatório Completo")
    win.geometry("620x380")
    win.configure(bg="#f0f0f0")
    win.grab_set()

    tk.Label(win, text="Relatório Completo de Aluguéis",
             font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)

    cols = ("Cliente", "Modelo", "Data Aluguel", "Data Devolução")
    tree = ttk.Treeview(win, columns=cols, show="headings", height=14)
    for c, w in zip(cols, [180, 130, 160, 160]):
        tree.heading(c, text=c); tree.column(c, width=w, anchor="center")
    tree.pack(padx=12, pady=4, fill="both", expand=True)

    try:
        con = conectar(); cur = con.cursor()
        cur.execute("""
            SELECT c.nome, b.modelo, a.data_aluguel, a.data_devolucao
            FROM alugueis a
            INNER JOIN clientes c ON a.fk_cliente = c.id_cliente
            INNER JOIN bicicletas b ON a.fk_bicicleta = b.id_bicicleta
        """)
        for r in cur.fetchall():
            tree.insert("", "end", values=r)
        con.close()
    except Exception as ex:
        messagebox.showerror("Erro", str(ex), parent=win)


# Clientes com aluguel
def abrir_clientes_com(pai):
    win = tk.Toplevel(pai)
    win.title("Clientes com Aluguel")
    win.geometry("380x340")
    win.configure(bg="#f0f0f0")
    win.grab_set()

    tk.Label(win, text="Clientes com Aluguel",
             font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)

    tree = ttk.Treeview(win, columns=("Nome",), show="headings", height=14)
    tree.heading("Nome", text="Nome"); tree.column("Nome", width=320, anchor="center")
    tree.pack(padx=12, pady=4, fill="both", expand=True)

    try:
        con = conectar(); cur = con.cursor()
        cur.execute("""
            SELECT DISTINCT c.nome
            FROM clientes c
            INNER JOIN alugueis a ON c.id_cliente = a.fk_cliente
        """)
        for r in cur.fetchall():
            tree.insert("", "end", values=r)
        con.close()
    except Exception as ex:
        messagebox.showerror("Erro", str(ex), parent=win)


#Clientes sem aluguel
def abrir_clientes_sem(pai):
    win = tk.Toplevel(pai)
    win.title("Clientes sem Aluguel")
    win.geometry("380x340")
    win.configure(bg="#f0f0f0")
    win.grab_set()

    tk.Label(win, text="Clientes sem Aluguel",
             font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)

    tree = ttk.Treeview(win, columns=("Nome",), show="headings", height=14)
    tree.heading("Nome", text="Nome"); tree.column("Nome", width=320, anchor="center")
    tree.pack(padx=12, pady=4, fill="both", expand=True)

    try:
        con = conectar(); cur = con.cursor()
        cur.execute("""
            SELECT c.nome
            FROM clientes c
            LEFT JOIN alugueis a ON c.id_cliente = a.fk_cliente
            WHERE a.id_aluguel IS NULL
        """)
        for r in cur.fetchall():
            tree.insert("", "end", values=r)
        con.close()
    except Exception as ex:
        messagebox.showerror("Erro", str(ex), parent=win)


# Histórico de cliente
def abrir_historico_cliente(pai):
    win = tk.Toplevel(pai)
    win.title("Histórico por Cliente")
    win.geometry("620x420")
    win.configure(bg="#f0f0f0")
    win.grab_set()

    tk.Label(win, text="Histórico por Cliente",
             font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)

    #Linha de busca
    bar = tk.Frame(win, bg="#f0f0f0"); bar.pack(pady=4)
    tk.Label(bar, text="Nome do cliente:", bg="#f0f0f0").pack(side="left", padx=4)
    e_busca = tk.Entry(bar, width=22); e_busca.pack(side="left", padx=4)

    cols = ("Cliente", "Modelo", "Data Aluguel")
    tree = ttk.Treeview(win, columns=cols, show="headings", height=14)
    for c, w in zip(cols, [180, 180, 200]):
        tree.heading(c, text=c); tree.column(c, width=w, anchor="center")
    tree.pack(padx=12, pady=6, fill="both", expand=True)

    def buscar():
        tree.delete(*tree.get_children())
        nome = e_busca.get().strip()
        filtro = f"%{nome}%" if nome else "%"
        try:
            con = conectar(); cur = con.cursor()
            cur.execute("""
                SELECT c.nome, b.modelo, a.data_aluguel
                FROM alugueis a
                INNER JOIN clientes c ON a.fk_cliente = c.id_cliente
                INNER JOIN bicicletas b ON a.fk_bicicleta = b.id_bicicleta
                WHERE c.nome ILIKE %s
                ORDER BY c.nome, a.data_aluguel DESC
            """, (filtro,))
            for r in cur.fetchall():
                tree.insert("", "end", values=r)
            con.close()
        except Exception as ex:
            messagebox.showerror("Erro", str(ex), parent=win)

    tk.Button(bar, text="Buscar", bg="#16a085", fg="white",
              width=10, command=buscar).pack(side="left", padx=4)

    buscar() 

if __name__ == "__main__":
    tela_login()