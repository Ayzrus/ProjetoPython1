import tkinter as tk
from tkinter import ttk
import mysql.connector
import ctypes
from tkcalendar import DateEntry
from datetime import datetime

desporto = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='desporto'
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

        for F in (StartPage, Page1, Page2, Page3, Page4, Page5, Page6):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont, values=None):
        frame = self.frames[cont]
        if values is not None and isinstance(frame, Page6):
            frame.set_values(values)
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Pagina Inicial", font=LARGEFONT)

        button1 = ttk.Button(self, text="Pavilhão",
                             command=lambda: controller.show_frame(Page1))

        button2 = ttk.Button(self, text="Equipa",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Jogos",
                             command=lambda: controller.show_frame(Page3))

        label.place(x=870, y=420)

        button1.place(x=900, y=460)

        button2.place(x=900, y=500)

        button3.place(x=900, y=540)


class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        voltar.grid(row=0, column=0, padx=10, pady=10)

        label = ttk.Label(self, text="Pavilhão", font=LARGEFONT)

        connection = desporto.cursor()

        values = []

        try:

            connection.execute("SELECT * FROM locais")

            for x in connection:
                values.append(x[1])

        except mysql.connector.Error as e:

            print(e)

        def criar_Pavilhao():

            selection = combo.get()

            value = entry.get()

            value2 = entry2.get()

            value3 = entry3.get()

            value4 = entry4.get()

            try:

                idLocal = 0

                connection.execute(f"SELECT * FROM locais WHERE Descricao = '{selection}'")

                for i in connection:
                    idLocal = i[0]

                values1 = (value, idLocal, value2, value3, value4)

                try:

                    connection.execute(f"INSERT INTO pavilhao (Descricao, Localicacao, Morada, Latitude, Longitude) "
                                       f"VALUES (%s, %s, %s, %s, %s)", values1)

                    desporto.commit()

                    print(connection.rowcount, "Pavilhao gravado com sucesso!")

                except mysql.connector.Error as ex1:

                    print(ex1)

            except mysql.connector.Error as ex:

                print(ex)

        combo = ttk.Combobox(
            self,
            state="readonly",
            values=values
        )

        button = ttk.Button(self, text="Criar Pavilhão", command=criar_Pavilhao)

        entry = ttk.Entry(self, width=23)

        entry2 = ttk.Entry(self, width=23)

        entry3 = ttk.Entry(self, width=23)

        entry4 = ttk.Entry(self, width=23)

        label.place(x=895, y=380)

        entry.place(x=870, y=420)

        combo.place(x=870, y=460)

        entry2.place(x=870, y=500)

        entry3.place(x=870, y=540)

        entry4.place(x=870, y=580)

        button.place(x=900, y=620)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Equipas", font=LARGEFONT)

        connection = desporto.cursor()

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        voltar.grid(row=1, column=1, padx=10, pady=10)

        def criar_Equipa():

            value = entry.get()

            value2 = entry2.get()

            values1 = (value, value2)

            try:

                connection.execute(f"INSERT INTO Equipa (Descricao, Clube) "
                                   f"VALUES (%s, %s)", values1)

                desporto.commit()

                print(connection.rowcount, "Equipa gravada com sucesso!")

            except mysql.connector.Error as ex1:

                print(ex1)

        entry = ttk.Entry(self, width=23)

        entry2 = ttk.Entry(self, width=23)

        button = ttk.Button(self, text="Criar Equipa", command=criar_Equipa)

        label.place(x=895, y=380)

        entry.place(x=870, y=420)

        entry2.place(x=870, y=460)

        button.place(x=900, y=500)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Jogos", font=LARGEFONT)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(StartPage))
        voltar.grid(row=1, column=1, padx=10, pady=10)

        button = ttk.Button(self, text="Adicionar",
                            command=lambda: controller.show_frame(Page4))

        button2 = ttk.Button(self, text="Resultados",
                             command=lambda: controller.show_frame(Page5))

        label.place(x=905, y=460)

        button.place(x=900, y=500)

        button2.place(x=900, y=540)


class Page4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(Page3))
        voltar.grid(row=1, column=1, padx=10, pady=10)

        connection = desporto.cursor()

        def update_combo2(event=None):
            selected_value = combo.get()
            combo2_values = [value for value in values if value != selected_value]
            combo2["values"] = combo2_values

        def criar_Jogo():
            data = cal.get()
            data_obj = datetime.strptime(data, '%m/%d/%y')
            data_formatada = data_obj.strftime('%Y-%m-%d')
            equipa1 = combo.get()
            equipa2 = combo2.get()
            pavilhao = combo3.get()
            idEquipa1 = 0
            idEquipa2 = 0
            idPavilhao = 0

            try:
                connection.execute(f"SELECT * FROM equipa WHERE Descricao = '{equipa1}'")
                for x1 in connection:
                    idEquipa1 = x1[0]
                connection.execute(f"SELECT * FROM equipa WHERE Descricao = '{equipa2}'")
                for x2 in connection:
                    idEquipa2 = x2[0]
                connection.execute(f"SELECT * FROM pavilhao WHERE Descricao = '{pavilhao}'")
                for x3 in connection:
                    idPavilhao = x3[0]
            except mysql.connector.Error as ex:
                print(ex)

            values1 = (idEquipa1, idEquipa2, data_formatada, idPavilhao)

            try:

                connection.execute(f"INSERT INTO jogo (Equipa1, Equipa2, Data, Pavilhao) "
                                   f"VALUES (%s, %s, %s, %s)", values1)

                desporto.commit()

                print(connection.rowcount, "Jogo gravado com sucesso!")

            except mysql.connector.Error as ex1:

                print(ex1)

        values = []

        values2 = []

        try:
            connection.execute("SELECT * FROM equipa")
            for x in connection:
                values.append(x[1])
        except mysql.connector.Error as e:
            print(e)
        try:
            connection.execute("SELECT * FROM pavilhao")
            for x in connection:
                values2.append(x[1])
        except mysql.connector.Error as e:
            print(e)

        combo = ttk.Combobox(
            self,
            state="readonly",
            values=values,
            postcommand=update_combo2
        )
        combo.bind("<<ComboboxSelected>>", update_combo2)

        combo2 = ttk.Combobox(
            self,
            state="readonly"
        )

        combo3 = ttk.Combobox(
            self,
            state="readonly",
            values=values2,
        )

        cal = DateEntry(self, width=20, background="magenta3", foreground="white", bd=2)

        button = ttk.Button(self, text="Criar Jogo", command=criar_Jogo)

        combo.place(x=870, y=460)

        combo2.place(x=870, y=500)

        combo3.place(x=870, y=540)

        cal.place(x=870, y=580)

        button.place(x=900, y=620)


class Page5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.tree = ttk.Treeview(self, columns=("Jogo", "Equipa1", "Equipa2"), show="headings")
        self.tree.heading("Jogo", text="Jogo")
        self.tree.heading("Equipa1", text="Equipa 1")
        self.tree.heading("Equipa2", text="Equipa 2")
        self.tree.place(x=650, y=540)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        label = ttk.Label(self, text="Equipas e Jogos", font=LARGEFONT)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(Page3))
        voltar.grid(row=1, column=1, padx=10, pady=10)

        label.place(x=865, y=460)

        self.listar()

    def on_tree_select(self, event):
        item_id = self.tree.focus()
        values = self.tree.item(item_id)['values']

        if values:
            Jogo, Equipa1, Equipa2 = values
            self.controller.show_frame(Page6, values=Jogo)

    def listar(self):
        connection = desporto.cursor()
        connection.execute("SELECT * FROM jogo")

        for row in self.tree.get_children():
            self.tree.delete(row)

        for x in connection:
            self.tree.insert("", "end", values=(x[0], x[1], x[2]))


class Page6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.values = 0

        label = ttk.Label(self, text="Adicionar Resultado", font=LARGEFONT)
        label.place(x=885, y=460)

        voltar = ttk.Button(self, text="Voltar",
                            command=lambda: controller.show_frame(Page5))
        voltar.grid(row=1, column=0, padx=10, pady=10)

        connection = desporto.cursor()

        def criar_Resultado():

            value = entry.get()

            value2 = entry2.get()

            values1 = (self.values, value, value2)

            try:
                print(values1)
                connection.execute(f"INSERT INTO resultado (IdJogo, PontosEq1, PontosEq2) "
                                   f"VALUES (%s, %s, %s)", values1)

                desporto.commit()

                print(connection.rowcount, "Resultado gravado com sucesso!")

            except mysql.connector.Error as ex1:

                print(ex1)

        entry = ttk.Entry(self, width=23)

        entry2 = ttk.Entry(self, width=23)

        button = ttk.Button(self, text="Registar Resultado", command=criar_Resultado)

        label.place(x=895, y=380)

        entry.place(x=930, y=420)

        entry2.place(x=930, y=460)

        button.place(x=950, y=500)

    def set_values(self, values):
        self.values = values
        self.show_values()

    def show_values(self):
        print(f"Id Jogo: {self.values}")


app = tkinterApp()
app.mainloop()
