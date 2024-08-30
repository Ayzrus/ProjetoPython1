import tkinter as tk
from tkinter import ttk
import mysql.connector
import ctypes
from tkcalendar import DateEntry
from datetime import datetime

lojaproduto = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='lojaprodutos'
)
LARGEFONT = ("Verdana", 15)


class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        taskbar_height = ctypes.windll.user32.GetSystemMetrics(4)

        self.geometry(f'{screen_width}x{screen_height - taskbar_height}')
        self.state('zoomed')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3, Page4, Page5, Page6, Page7):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Pagina Inicial", font=LARGEFONT)

        button1 = ttk.Button(self, text="Registar Compras",
                             command=lambda: controller.show_frame(Page1))

        button2 = ttk.Button(self, text="Registar Produtos",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Adicionar Produtos às Compras",
                             command=lambda: controller.show_frame(Page3))

        button4 = ttk.Button(self, text="Alterar Estado das compras",
                             command=lambda: controller.show_frame(Page4))

        button5 = ttk.Button(self, text="Adicionar Stock dos produtos",
                             command=lambda: controller.show_frame(Page5))

        button6 = ttk.Button(self, text="Listagem de stocks",
                             command=lambda: controller.show_frame(Page6))

        button7 = ttk.Button(self, text="Listagem de stocks com produtos abaixo do stock mínimo",
                             command=lambda: controller.show_frame(Page7))

        label.place(x=870, y=420)

        button1.place(x=900, y=460)

        button2.place(x=900, y=500)

        button3.place(x=865, y=540)

        button4.place(x=880, y=580)

        button5.place(x=872, y=620)

        button6.place(x=900, y=660)

        button7.place(x=800, y=700)


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        connection = lojaproduto.cursor()

        def guardar_compra():
            data = cal.get()
            data_obj = datetime.strptime(data, '%m/%d/%y')
            data_formatada = data_obj.strftime('%Y-%m-%d')
            Descricao = entry.get()

            values1 = (Descricao, data_formatada)

            try:

                connection.execute(f"INSERT INTO compras (Descricao, Data, Id_Estado) "
                                   f"VALUES (%s, %s, 1)", values1)

                lojaproduto.commit()

                print(connection.rowcount, "Compra gravado com sucesso!")

            except mysql.connector.Error as ex:

                print(ex)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        voltar.grid(row=1, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Registar Compras",
                             command=lambda: controller.show_frame(Page1))

        button2 = ttk.Button(self, text="Registar Produtos",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Adicionar Produtos às Compras",
                             command=lambda: controller.show_frame(Page3))

        button4 = ttk.Button(self, text="Alterar Estado das compras",
                             command=lambda: controller.show_frame(Page4))

        button5 = ttk.Button(self, text="Adicionar Stock dos produtos",
                             command=lambda: controller.show_frame(Page5))

        button6 = ttk.Button(self, text="Listagem de stocks",
                             command=lambda: controller.show_frame(Page6))

        button7 = ttk.Button(self, text="Listagem de stocks com produtos abaixo do stock mínimo",
                             command=lambda: controller.show_frame(Page7))

        button1.grid(row=2, column=1, padx=10, pady=10)

        button2.grid(row=3, column=1, padx=10, pady=10)

        button3.grid(row=4, column=1, padx=10, pady=10)

        button4.grid(row=5, column=1, padx=10, pady=10)

        button5.grid(row=6, column=1, padx=10, pady=10)

        button6.grid(row=7, column=1, padx=10, pady=10)

        button7.grid(row=8, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="Registar Compras", font=LARGEFONT)

        label2 = ttk.Label(self, text="Descrição", font=LARGEFONT)

        label3 = ttk.Label(self, text="Data", font=LARGEFONT)

        cal = DateEntry(self, width=20, background="magenta3", foreground="white", bd=2)

        entry = ttk.Entry(self, width=23)

        button = ttk.Button(self, text="Guardar", command=guardar_compra)

        label.place(x=900, y=420)

        label2.place(x=940, y=460)

        entry.place(x=920, y=500)

        label3.place(x=965, y=520)

        cal.place(x=920, y=560)

        button.place(x=960, y=600)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        values = []

        connection = lojaproduto.cursor()

        try:

            connection.execute("SELECT * FROM fornecedor")

            for x in connection:
                values.append(x[4])

        except mysql.connector.Error as e:

            print(e)

        def guardar_produto():
            descricao = entry.get()
            preco_compra = entry2.get()
            id_fornecedor = 0
            preco_venda = entry3.get()
            stock_minimo = entry4.get()

            try:

                connection.execute("SELECT * FROM fornecedor")

                for xy in connection:
                    if xy[4] == combo.get():
                        id_fornecedor = xy[0]

            except mysql.connector.Error as ex:

                print(ex)

            values1 = (descricao, preco_compra, id_fornecedor, preco_venda, stock_minimo)

            try:

                connection.execute(f"INSERT INTO produto "
                                   f"(Descricao, Preco_compra, Id_fornecedor, Preco_venda, Stock_minimo) "
                                   f"VALUES (%s, %s, %s, %s, %s)", values1)

                lojaproduto.commit()

                print(connection.rowcount, "Produto gravado com sucesso!")

            except mysql.connector.Error as ex:

                print(ex)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        voltar.grid(row=1, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Registar Compras",
                             command=lambda: controller.show_frame(Page1))

        button2 = ttk.Button(self, text="Registar Produtos",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Adicionar Produtos às Compras",
                             command=lambda: controller.show_frame(Page3))

        button4 = ttk.Button(self, text="Alterar Estado das compras",
                             command=lambda: controller.show_frame(Page4))

        button5 = ttk.Button(self, text="Adicionar Stock dos produtos",
                             command=lambda: controller.show_frame(Page5))

        button6 = ttk.Button(self, text="Listagem de stocks",
                             command=lambda: controller.show_frame(Page6))

        button7 = ttk.Button(self, text="Listagem de stocks com produtos abaixo do stock mínimo",
                             command=lambda: controller.show_frame(Page7))

        button1.grid(row=2, column=1, padx=10, pady=10)

        button2.grid(row=3, column=1, padx=10, pady=10)

        button3.grid(row=4, column=1, padx=10, pady=10)

        button4.grid(row=5, column=1, padx=10, pady=10)

        button5.grid(row=6, column=1, padx=10, pady=10)

        button6.grid(row=7, column=1, padx=10, pady=10)

        button7.grid(row=8, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="Registar Produtos", font=LARGEFONT)

        label2 = ttk.Label(self, text="Descrição", font=LARGEFONT)

        label3 = ttk.Label(self, text="Preço de Compra", font=LARGEFONT)

        label4 = ttk.Label(self, text="Fornecedor", font=LARGEFONT)

        label5 = ttk.Label(self, text="Preço de Venda", font=LARGEFONT)

        label6 = ttk.Label(self, text="Stock Minimo", font=LARGEFONT)

        entry = ttk.Entry(self, width=23)

        entry2 = ttk.Entry(self, width=23)

        entry3 = ttk.Entry(self, width=23)

        entry4 = ttk.Entry(self, width=23)

        combo = ttk.Combobox(
            self,
            state="readonly",
            values=values
        )

        button = ttk.Button(self, text="Guardar", command=guardar_produto)

        label.place(x=900, y=420)

        label2.place(x=920, y=460)

        entry.place(x=920, y=500)

        label3.place(x=920, y=540)

        entry2.place(x=920, y=580)

        label4.place(x=920, y=620)

        combo.place(x=920, y=660)

        label5.place(x=920, y=700)

        entry3.place(x=920, y=740)

        label6.place(x=920, y=780)

        entry4.place(x=920, y=820)

        button.place(x=955, y=860)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        values = []

        values1 = []

        connection = lojaproduto.cursor()

        def guardar_produto_compra():
            id_prod = 0
            id_compra = 0

            try:

                connection.execute("SELECT * FROM compras")

                for xu in connection:
                    if xu[1] == combo.get():
                        id_compra = xu[0]

                connection.execute("SELECT * FROM produto")

                for xp in connection:
                    if xp[1] == combo2.get():
                        id_prod = xp[0]

            except mysql.connector.Error as eu:

                print(eu)

            values3 = (id_prod, id_compra, entry.get())

            try:

                connection.execute(f"INSERT INTO produto_compras (id_prod, id_compra, quantidade) "
                                   f"VALUES (%s, %s, %s)", values3)

                lojaproduto.commit()

                print(connection.rowcount, "Produto_compras gravado com sucesso!")

            except mysql.connector.Error as ex:

                print(ex)

        try:

            connection.execute("SELECT * FROM compras")

            for x in connection:
                values.append(x[1])

            connection.execute("SELECT * FROM produto")

            for xe in connection:
                values1.append(xe[1])

        except mysql.connector.Error as e:

            print(e)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        voltar.grid(row=1, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Registar Compras",
                             command=lambda: controller.show_frame(Page1))

        button2 = ttk.Button(self, text="Registar Produtos",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Adicionar Produtos às Compras",
                             command=lambda: controller.show_frame(Page3))

        button4 = ttk.Button(self, text="Alterar Estado das compras",
                             command=lambda: controller.show_frame(Page4))

        button5 = ttk.Button(self, text="Adicionar Stock dos produtos",
                             command=lambda: controller.show_frame(Page5))

        button6 = ttk.Button(self, text="Listagem de stocks",
                             command=lambda: controller.show_frame(Page6))

        button7 = ttk.Button(self, text="Listagem de stocks com produtos abaixo do stock mínimo",
                             command=lambda: controller.show_frame(Page7))

        button1.grid(row=2, column=1, padx=10, pady=10)

        button2.grid(row=3, column=1, padx=10, pady=10)

        button3.grid(row=4, column=1, padx=10, pady=10)

        button4.grid(row=5, column=1, padx=10, pady=10)

        button5.grid(row=6, column=1, padx=10, pady=10)

        button6.grid(row=7, column=1, padx=10, pady=10)

        button7.grid(row=8, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="Adicionar Produtos às Compras", font=LARGEFONT)

        label2 = ttk.Label(self, text="Compra", font=LARGEFONT)

        label3 = ttk.Label(self, text="Produto", font=LARGEFONT)

        label4 = ttk.Label(self, text="Quantidade", font=LARGEFONT)

        button = ttk.Button(self, text="Guardar", command=guardar_produto_compra)

        combo = ttk.Combobox(
            self,
            state="readonly",
            values=values
        )

        combo2 = ttk.Combobox(
            self,
            state="readonly",
            values=values1
        )

        entry = ttk.Entry(self, width=23)

        label.place(x=820, y=420)

        label2.place(x=900, y=460)

        combo.place(x=900, y=500)

        label3.place(x=900, y=540)

        combo2.place(x=900, y=580)

        label4.place(x=900, y=620)

        entry.place(x=900, y=660)

        button.place(x=940, y=700)


class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        voltar.grid(row=1, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Registar Compras",
                             command=lambda: controller.show_frame(Page1))

        button2 = ttk.Button(self, text="Registar Produtos",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Adicionar Produtos às Compras",
                             command=lambda: controller.show_frame(Page3))

        button4 = ttk.Button(self, text="Alterar Estado das compras",
                             command=lambda: controller.show_frame(Page4))

        button5 = ttk.Button(self, text="Adicionar Stock dos produtos",
                             command=lambda: controller.show_frame(Page5))

        button6 = ttk.Button(self, text="Listagem de stocks",
                             command=lambda: controller.show_frame(Page6))

        button7 = ttk.Button(self, text="Listagem de stocks com produtos abaixo do stock mínimo",
                             command=lambda: controller.show_frame(Page7))

        button1.grid(row=2, column=1, padx=10, pady=10)

        button2.grid(row=3, column=1, padx=10, pady=10)

        button3.grid(row=4, column=1, padx=10, pady=10)

        button4.grid(row=5, column=1, padx=10, pady=10)

        button5.grid(row=6, column=1, padx=10, pady=10)

        button6.grid(row=7, column=1, padx=10, pady=10)

        button7.grid(row=8, column=1, padx=10, pady=10)

        values = []

        values1 = []

        connection = lojaproduto.cursor()

        def alterar_estado():
            id_compra = 0
            id_estado = 0
            values3 = []

            try:

                connection.execute("SELECT * FROM compras")

                for xc in connection:
                    if xc[1] == combo.get():
                        id_compra = xc[0]

                connection.execute("SELECT * FROM estado")

                for xes in connection:
                    if xes[1] == combo2.get():
                        id_estado = xes[0]

            except mysql.connector.Error as eu:

                print(eu)

            try:

                connection.execute(f"UPDATE `compras` SET `Id_Estado`='{id_estado}' WHERE Id = {id_compra}")

                lojaproduto.commit()

                print(connection.rowcount, "compras alterada com sucesso!")

                if connection.rowcount > 0:
                    try:

                        connection.execute(f"SELECT * FROM produto_compras WHERE Id_compra = {id_compra}")
                        values3 = []
                        for xce in connection:
                            values3.append({1: xce[1], 2: xce[3]})

                    except mysql.connector.Error as eu:

                        print(eu)

                    if id_estado == 1:
                        for p in values3:
                            connection.execute(f"SELECT * FROM Stock "
                                               f"WHERE Id_prod = {p[1]}")
                            qtd = 0
                            for qd in connection:
                                qtd = qd[2]
                            if connection.rowcount > 0:
                                try:

                                    total = qtd - p[2]

                                    connection.execute(f"UPDATE stock SET Quantidade='{total}'"
                                                       f" WHERE Id_prod = {p[1]}")

                                    print(connection.rowcount, "Reduzido com sucesso!")

                                    lojaproduto.commit()

                                except mysql.connector.Error as ex:
                                    print(ex)
                            else:
                                connection.execute(
                                    f"INSERT INTO stock (Id_prod, Quantidade) "
                                    f"VALUES ('{p[1]}','{p[2]}')")

                                lojaproduto.commit()

                                print(connection.rowcount, "Adicionado alterada com sucesso!")
                    elif id_estado == 2:
                        for p in values3:

                            connection.execute(f"SELECT * FROM Stock "
                                               f"WHERE Id_prod = {p[1]}")
                            qtd = 0

                            for qd in connection:

                                qtd = qd[2]

                            if connection.rowcount > 0:

                                try:
                                    total = qtd + p[2]

                                    connection.execute(f"UPDATE stock SET Quantidade='{total}'"
                                                       f" WHERE Id_prod = {p[1]}")

                                    lojaproduto.commit()

                                    print(connection.rowcount, "Somado com sucesso!")

                                except mysql.connector.Error as ex:
                                    print(ex)
                            else:
                                connection.execute(
                                    f"INSERT INTO stock (Id_prod, Quantidade) "
                                    f"VALUES ('{p[1]}','{p[2]}')")

                                lojaproduto.commit()

                                print(connection.rowcount, "Adicionado alterada com sucesso!")

            except mysql.connector.Error as ex:

                print(ex)

        try:

            connection.execute("SELECT * FROM compras")

            for x in connection:
                values.append(x[1])

            connection.execute("SELECT * FROM estado")

            for xe in connection:
                values1.append(xe[1])

        except mysql.connector.Error as e:

            print(e)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        voltar.grid(row=1, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Registar Compras",
                             command=lambda: controller.show_frame(Page1))

        button2 = ttk.Button(self, text="Registar Produtos",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Adicionar Produtos às Compras",
                             command=lambda: controller.show_frame(Page3))

        button4 = ttk.Button(self, text="Alterar Estado das compras",
                             command=lambda: controller.show_frame(Page4))

        button5 = ttk.Button(self, text="Adicionar Stock dos produtos",
                             command=lambda: controller.show_frame(Page5))

        button6 = ttk.Button(self, text="Listagem de stocks",
                             command=lambda: controller.show_frame(Page6))

        button7 = ttk.Button(self, text="Listagem de stocks com produtos abaixo do stock mínimo",
                             command=lambda: controller.show_frame(Page7))

        button1.grid(row=2, column=1, padx=10, pady=10)

        button2.grid(row=3, column=1, padx=10, pady=10)

        button3.grid(row=4, column=1, padx=10, pady=10)

        button4.grid(row=5, column=1, padx=10, pady=10)

        button5.grid(row=6, column=1, padx=10, pady=10)

        button6.grid(row=7, column=1, padx=10, pady=10)

        button7.grid(row=8, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="Adicionar Produtos às Compras", font=LARGEFONT)

        label2 = ttk.Label(self, text="Compra", font=LARGEFONT)

        label3 = ttk.Label(self, text="Estado", font=LARGEFONT)

        button = ttk.Button(self, text="Guardar", command=alterar_estado)

        combo = ttk.Combobox(
            self,
            state="readonly",
            values=values
        )

        combo2 = ttk.Combobox(
            self,
            state="readonly",
            values=values1
        )

        label.place(x=820, y=420)

        label2.place(x=900, y=460)

        combo.place(x=900, y=500)

        label3.place(x=900, y=540)

        combo2.place(x=900, y=580)

        button.place(x=940, y=620)


class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        values = []

        connection = lojaproduto.cursor()

        try:

            connection.execute("SELECT * FROM produto")

            for x in connection:
                values.append(x[1])

        except mysql.connector.Error as e:

            print(e)

        def alterar_stock():
            id_prod = 0

            try:

                connection.execute("SELECT * FROM produto")

                for xe in connection:
                    if xe[1] == combo.get():
                        id_prod = xe[0]

            except mysql.connector.Error as ex:

                print(ex)

            try:

                connection.execute(f"SELECT * FROM Stock "
                                   f"WHERE Id_prod = {id_prod}")

                for xex in connection:
                    if xex[1] == id_prod:
                        try:

                            connection.execute(f"UPDATE stock SET Quantidade='{entry.get()}'"
                                               f" WHERE Id_prod = {id_prod}")

                            lojaproduto.commit()

                            print(connection.rowcount, "Editado com sucesso!")

                        except mysql.connector.Error as ex:
                            print(ex)
                    else:
                        try:
                            connection.execute(
                                f"INSERT INTO stock (Id_prod, Quantidade) "
                                f"VALUES ('{id_prod}','{entry.get()}')")

                            lojaproduto.commit()

                            print(connection.rowcount, "Adicionado alterada com sucesso!")
                        except mysql.connector.Error as ex:
                            print(ex)

            except mysql.connector.Error as ex:

                print(ex)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        voltar.grid(row=1, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Registar Compras",
                             command=lambda: controller.show_frame(Page1))

        button2 = ttk.Button(self, text="Registar Produtos",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Adicionar Produtos às Compras",
                             command=lambda: controller.show_frame(Page3))

        button4 = ttk.Button(self, text="Alterar Estado das compras",
                             command=lambda: controller.show_frame(Page4))

        button5 = ttk.Button(self, text="Adicionar Stock dos produtos",
                             command=lambda: controller.show_frame(Page5))

        button6 = ttk.Button(self, text="Listagem de stocks",
                             command=lambda: controller.show_frame(Page6))

        button7 = ttk.Button(self, text="Listagem de stocks com produtos abaixo do stock mínimo",
                             command=lambda: controller.show_frame(Page7))

        button1.grid(row=2, column=1, padx=10, pady=10)

        button2.grid(row=3, column=1, padx=10, pady=10)

        button3.grid(row=4, column=1, padx=10, pady=10)

        button4.grid(row=5, column=1, padx=10, pady=10)

        button5.grid(row=6, column=1, padx=10, pady=10)

        button6.grid(row=7, column=1, padx=10, pady=10)

        button7.grid(row=8, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="Adicionar Stock dos produtos", font=LARGEFONT)

        label2 = ttk.Label(self, text="Produto", font=LARGEFONT)

        label3 = ttk.Label(self, text="Stock", font=LARGEFONT)

        button = ttk.Button(self, text="Guardar", command=alterar_stock)

        combo = ttk.Combobox(
            self,
            state="readonly",
            values=values
        )

        entry = ttk.Entry(self, width=23)

        label.place(x=820, y=420)

        label2.place(x=900, y=460)

        combo.place(x=900, y=500)

        label3.place(x=900, y=540)

        entry.place(x=900, y=580)

        button.place(x=940, y=620)


class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.tree = ttk.Treeview(self, columns=("Produto", "Quantidade"), show="headings")
        self.tree.heading("Produto", text="Produto")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.place(x=800, y=540)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        voltar.grid(row=1, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Registar Compras",
                             command=lambda: controller.show_frame(Page1))

        button2 = ttk.Button(self, text="Registar Produtos",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Adicionar Produtos às Compras",
                             command=lambda: controller.show_frame(Page3))

        button4 = ttk.Button(self, text="Alterar Estado das compras",
                             command=lambda: controller.show_frame(Page4))

        button5 = ttk.Button(self, text="Adicionar Stock dos produtos",
                             command=lambda: controller.show_frame(Page5))

        button6 = ttk.Button(self, text="Listagem de stocks",
                             command=lambda: controller.show_frame(Page6))

        button7 = ttk.Button(self, text="Listagem de stocks com produtos abaixo do stock mínimo",
                             command=lambda: controller.show_frame(Page7))

        button1.grid(row=2, column=1, padx=10, pady=10)

        button2.grid(row=3, column=1, padx=10, pady=10)

        button3.grid(row=4, column=1, padx=10, pady=10)

        button4.grid(row=5, column=1, padx=10, pady=10)

        button5.grid(row=6, column=1, padx=10, pady=10)

        button6.grid(row=7, column=1, padx=10, pady=10)

        button7.grid(row=8, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="Listagem de stocks", font=LARGEFONT)

        label.place(x=910, y=500)

        self.listar()

    def listar(self):
        connection = lojaproduto.cursor()
        connection.execute("SELECT P.Descricao ,S.Quantidade FROM stock S LEFT JOIN Produto P ON P.Id = S.Id_prod")

        for row in self.tree.get_children():
            self.tree.delete(row)

        for x in connection:
            self.tree.insert("", "end", values=(x[0], x[1]))


class Page7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.tree = ttk.Treeview(self, columns=("Produto", "Quantidade"), show="headings")
        self.tree.heading("Produto", text="Produto")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.place(x=800, y=540)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        voltar.grid(row=1, column=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="Registar Compras",
                             command=lambda: controller.show_frame(Page1))

        button2 = ttk.Button(self, text="Registar Produtos",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Adicionar Produtos às Compras",
                             command=lambda: controller.show_frame(Page3))

        button4 = ttk.Button(self, text="Alterar Estado das compras",
                             command=lambda: controller.show_frame(Page4))

        button5 = ttk.Button(self, text="Adicionar Stock dos produtos",
                             command=lambda: controller.show_frame(Page5))

        button6 = ttk.Button(self, text="Listagem de stocks",
                             command=lambda: controller.show_frame(Page6))

        button7 = ttk.Button(self, text="Listagem de stocks com produtos abaixo do stock mínimo",
                             command=lambda: controller.show_frame(Page7))

        button1.grid(row=2, column=1, padx=10, pady=10)

        button2.grid(row=3, column=1, padx=10, pady=10)

        button3.grid(row=4, column=1, padx=10, pady=10)

        button4.grid(row=5, column=1, padx=10, pady=10)

        button5.grid(row=6, column=1, padx=10, pady=10)

        button6.grid(row=7, column=1, padx=10, pady=10)

        button7.grid(row=8, column=1, padx=10, pady=10)

        label = ttk.Label(self, text="Listagem de stocks com produtos abaixo do stock mínimo", font=LARGEFONT)

        label.place(x=800, y=500)

        self.listar()

    def listar(self):
        connection = lojaproduto.cursor()
        connection.execute("SELECT P.Descricao, S.Quantidade FROM stock S LEFT JOIN Produto P ON P.Id = S.Id_prod"
                           " WHERE S.Quantidade < P.Stock_minimo")

        for row in self.tree.get_children():
            self.tree.delete(row)

        for x in connection:
            self.tree.insert("", "end", values=(x[0], x[1]))


app = tkinterApp()
app.mainloop()
