import tkinter as tk
from tkinter import ttk
import mysql.connector

lojapy = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='lojapy'
)
LARGEFONT = ("Verdana", 15)


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def listar_page3(self):
        page3_instance = self.frames[Page3]


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Pagina Inicial", font=LARGEFONT)

        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Clientes",
                             command=lambda: controller.show_frame(Page1))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Produto",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Vendas",
                             command=lambda: controller.show_frame(Page3))

        button2.grid(row=2, column=1, padx=10, pady=10)

        button3.grid(row=3, column=1, padx=10, pady=10)


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def registarCliente():
            nif = entry.get()
            email = entry2.get()
            morada = entry3.get()
            tel = entry4.get()
            nome = entry5.get()

            connection = lojapy.cursor()

            values = (nif, nome, morada, tel, email)

            try:

                connection.execute("INSERT INTO Cliente (Nif, Nome, Morada, Tel, Email) "
                                   "VALUES (%s, %s, %s, %s, %s)", values)

                lojapy.commit()

                print(connection.rowcount, "Cliente gravado com sucesso!")

            except mysql.connector.Error as e:

                print(e)

        label = ttk.Label(self, text="Clientes", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Pagina Inicial",
                             command=lambda: controller.show_frame(StartPage))

        text2 = ttk.Label(self, text="Insira o Nif")
        text2.grid(column=0, row=0, padx=10, pady=10)

        entry = ttk.Entry(self, width=45)
        entry.grid(column=0, row=1, padx=10, pady=10)

        text2 = ttk.Label(self, text="Insira o Email")
        text2.grid(column=0, row=2, padx=10, pady=10)

        entry2 = ttk.Entry(self, width=45)
        entry2.grid(column=0, row=3, padx=10, pady=10)

        text3 = ttk.Label(self, text="Insira a Morada")
        text3.grid(column=0, row=4, padx=10, pady=10)

        entry3 = ttk.Entry(self, width=45)
        entry3.grid(column=0, row=5, padx=10, pady=10)

        text4 = ttk.Label(self, text="Insira o Telefone")
        text4.grid(column=0, row=6, padx=10, pady=10)
        entry4 = ttk.Entry(self, width=45)
        entry4.grid(column=0, row=7, padx=10, pady=10)

        text5 = ttk.Label(self, text="Insira o Nome")
        text5.grid(column=0, row=8, padx=10, pady=10)
        entry5 = ttk.Entry(self, width=45)
        entry5.grid(column=0, row=9, padx=10, pady=10)

        button = ttk.Button(self, text="Registar", command=registarCliente)
        button.grid(row=10, column=0, padx=10, pady=10)

        text_response = ttk.Label(self, text="")
        text_response.grid(column=0, row=2, padx=10, pady=10)

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Vendas",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Produto",
                             command=lambda: controller.show_frame(Page3))

        button2.grid(row=2, column=1, padx=10, pady=10)

        button3.grid(row=3, column=1, padx=10, pady=10)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def registarProduto():
            ref = entry.get()
            descricao = entry2.get()
            preco = entry3.get()

            connection = lojapy.cursor()

            values = (ref, descricao, preco)

            try:

                connection.execute("INSERT INTO Produto (Ref, Descricao, Preco) "
                                   "VALUES (%s, %s , %s)", values)

                lojapy.commit()

                print(connection.rowcount, "Produto gravado com sucesso!")

            except mysql.connector.Error as e:

                print(e)

        label = ttk.Label(self, text="Produto", font=LARGEFONT)

        label.grid(row=0, column=4, padx=10, pady=10)

        text2 = ttk.Label(self, text="Insira a Ref do produto")
        text2.grid(column=0, row=0, padx=10, pady=10)

        entry = ttk.Entry(self, width=45)
        entry.grid(column=0, row=1, padx=10, pady=10)

        text2 = ttk.Label(self, text="Insira a Descrição")
        text2.grid(column=0, row=2, padx=10, pady=10)

        entry2 = ttk.Entry(self, width=45)
        entry2.grid(column=0, row=3, padx=10, pady=10)

        text3 = ttk.Label(self, text="Insira a Descrição")
        text3.grid(column=0, row=4, padx=10, pady=10)

        entry3 = ttk.Entry(self, width=45)
        entry3.grid(column=0, row=5, padx=10, pady=10)

        button = ttk.Button(self, text="Registar", command=registarProduto)
        button.grid(row=6, column=0, padx=10, pady=10)

        button1 = ttk.Button(self, text="Clientes",
                             command=lambda: controller.show_frame(Page1))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Pagina Inicial",
                             command=lambda: controller.show_frame(StartPage))

        button3 = ttk.Button(self, text="Vendas",
                             command=lambda: controller.show_frame(Page3))

        button2.grid(row=2, column=1, padx=10, pady=10)

        button3.grid(row=3, column=1, padx=10, pady=10)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label5 = None

        self.tree = ttk.Treeview(self, columns=("Id_cliente", "Id_venda"), show="headings")
        self.tree.heading("Id_cliente", text="Id Cliente")
        self.tree.heading("Id_venda", text="Id Venda")
        self.tree.grid(row=15, column=0, columnspan=3, padx=10, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.product_tree = ttk.Treeview(self, columns=("Ref", "Descricao", "Preco", "Total", "TotalcomIva"),
                                         show="headings")
        self.product_tree.heading("Ref", text="Ref")
        self.product_tree.heading("Descricao", text="Descrição")
        self.product_tree.heading("Preco", text="Preço")
        self.product_tree.heading("Total", text="Total")
        self.product_tree.heading("TotalcomIva", text="Total com Iva")
        self.product_tree.grid(row=17, column=0, columnspan=5, padx=10, pady=10)

        self.product_tree.bind("<<TreeviewSelect>>", self.on_product_tree_select)

        def registarVenda(estado):
            if estado:
                Num = entry.get()
                IdCliente = entry2.get()

                connection = lojapy.cursor()

                values = (Num, IdCliente)

                try:

                    connection.execute("INSERT INTO Venda (Num, Id_Cliente) "
                                       "VALUES (%s, %s)", values)

                    lojapy.commit()

                    print(connection.rowcount, "Venda gravado com sucesso!")

                except mysql.connector.Error as e:

                    print(e)
            else:
                connection = lojapy.cursor()
                IdVenda = entry5.get()
                IdProduto = entry3.get()
                Quantidade = entry4.get()
                values2 = (IdProduto, IdVenda, Quantidade)
                try:

                    connection.execute("INSERT INTO venda_prod (IdProd, IdVenda, Quantidade) "
                                       "VALUES (%s, %s, %s)", values2)

                    lojapy.commit()

                    print(connection.rowcount, "Venda prod gravado com sucesso!")

                except mysql.connector.Error as e:

                    print(e)

        label = ttk.Label(self, text="Vendas", font=LARGEFONT)

        label.grid(row=0, column=4, padx=10, pady=10)

        text2 = ttk.Label(self, text="Insira o Num da venda")
        text2.grid(column=0, row=0, padx=10, pady=10)

        entry = ttk.Entry(self, width=45)
        entry.grid(column=0, row=1, padx=10, pady=10)

        text2 = ttk.Label(self, text="Insira o Id do Cliente")
        text2.grid(column=0, row=2, padx=10, pady=10)

        entry2 = ttk.Entry(self, width=45)
        entry2.grid(column=0, row=3, padx=10, pady=10)

        text5 = ttk.Label(self, text="Insira o Id Venda do produto")
        text5.grid(column=0, row=9, padx=10, pady=10)

        entry5 = ttk.Entry(self, width=45)
        entry5.grid(column=0, row=10, padx=10, pady=10)

        text3 = ttk.Label(self, text="Insira a Ref do produto")
        text3.grid(column=0, row=4, padx=10, pady=10)

        entry3 = ttk.Entry(self, width=45)
        entry3.grid(column=0, row=5, padx=10, pady=10)

        text4 = ttk.Label(self, text="Insira a Quantidade")
        text4.grid(column=0, row=6, padx=10, pady=10)

        entry4 = ttk.Entry(self, width=45)
        entry4.grid(column=0, row=7, padx=10, pady=10)

        button = ttk.Button(self, text="Registar", command=lambda: registarVenda(True))
        button.grid(row=8, column=0, padx=10, pady=10)
        button = ttk.Button(self, text="Registar venda produto", command=lambda: registarVenda(False))
        button.grid(row=11, column=0, padx=10, pady=10)

        button1 = ttk.Button(self, text="Clientes",
                             command=lambda: controller.show_frame(Page1))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Pagina Inicial",
                             command=lambda: controller.show_frame(StartPage))

        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Produto",
                             command=lambda: controller.show_frame(Page2))

        button3.grid(row=3, column=1, padx=10, pady=10)

        button5 = ttk.Button(self, text="Listar Vendas",
                             command=lambda: self.listar())
        button5.grid(row=4, column=1, padx=10, pady=10)

    def on_row_click(self, id_venda):
        for row in self.product_tree.get_children():
            self.product_tree.delete(row)

        values = (id_venda,)
        connection = lojapy.cursor()
        connection.execute("SELECT p.Ref, P.Descricao, P.Preco, P.Preco * 1.23 AS Iva"
                           " FROM produto P"
                           " LEFT JOIN venda_prod VP ON P.Ref = VP.IdProd"
                           " WHERE VP.IdVenda = %s", values)
        total = []
        totaliva = []
        for x in connection:
            if connection.rowcount == 1:
                total.append(x[2])
                totaliva.append(x[3])
                self.product_tree.insert("", "end", values=(x[0], x[1], x[2], 0, 0))
            else:
                total2 = total[0] + x[2]
                totaliva2 = totaliva[0] + x[3]
                self.product_tree.insert("", "end", values=(x[0], x[1], x[2], total2, totaliva2))

    def on_product_tree_select(self, event):
        item_id = self.product_tree.focus()
        values = self.product_tree.item(item_id)['values']

    def listar(self):
        connection = lojapy.cursor()
        connection.execute("SELECT * FROM Venda")

        for row in self.tree.get_children():
            self.tree.delete(row)

        for x in connection:
            print(x)
            self.tree.insert("", "end", values=(x[1], x[0]))

    def on_tree_select(self, event):
        item_id = self.tree.focus()

        values = self.tree.item(item_id)['values']

        if values:
            id_cliente, id_venda = values
            self.on_row_click(id_venda)


app = tkinterApp()
app.mainloop()
app.attributes('-fullscreen', True)
