import tkinter as tk
from tkinter import ttk
import mysql.connector

hotel = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='hotel'
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


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Pagina Inicial", font=LARGEFONT)

        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Clientes",
                             command=lambda: controller.show_frame(Page1))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Quartos",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Reservas",
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

            connection = hotel.cursor()

            values = (nif, morada, email)

            try:

                connection.execute("INSERT INTO Cliente (Nif, Morada, Email) "
                                   "VALUES (%s, %s, %s)", values)

                hotel.commit()

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

        button = ttk.Button(self, text="Registar", command=registarCliente)
        button.grid(row=6, column=0, padx=10, pady=10)

        text_response = ttk.Label(self, text="")
        text_response.grid(column=0, row=2, padx=10, pady=10)

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Quartos",
                             command=lambda: controller.show_frame(Page2))

        button3 = ttk.Button(self, text="Reservas",
                             command=lambda: controller.show_frame(Page3))

        button2.grid(row=2, column=1, padx=10, pady=10)

        button3.grid(row=3, column=1, padx=10, pady=10)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def registarQuarto():
            numeroQuarto = entry.get()
            idTipo = entry2.get()

            connection = hotel.cursor()

            values = (numeroQuarto, idTipo)

            try:

                connection.execute("INSERT INTO Quarto (Numero, Id_Tipo) "
                                   "VALUES (%s, %s)", values)

                hotel.commit()

                print(connection.rowcount, "Quarto gravado com sucesso!")

            except mysql.connector.Error as e:

                print(e)

        label = ttk.Label(self, text="Quartos", font=LARGEFONT)

        label.grid(row=0, column=4, padx=10, pady=10)

        text2 = ttk.Label(self, text="Insira o Numero do quarto")
        text2.grid(column=0, row=0, padx=10, pady=10)

        entry = ttk.Entry(self, width=45)
        entry.grid(column=0, row=1, padx=10, pady=10)

        text2 = ttk.Label(self, text="Insira o Id do Tipo")
        text2.grid(column=0, row=2, padx=10, pady=10)

        entry2 = ttk.Entry(self, width=45)
        entry2.grid(column=0, row=3, padx=10, pady=10)

        button = ttk.Button(self, text="Registar", command=registarQuarto)
        button.grid(row=6, column=0, padx=10, pady=10)

        button1 = ttk.Button(self, text="Clientes",
                             command=lambda: controller.show_frame(Page1))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Pagina Inicial",
                             command=lambda: controller.show_frame(StartPage))

        button3 = ttk.Button(self, text="Reservas",
                             command=lambda: controller.show_frame(Page3))

        button2.grid(row=2, column=1, padx=10, pady=10)

        button3.grid(row=3, column=1, padx=10, pady=10)


class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def registarReserva():
            idcliente = entry.get()
            idquarto = entry2.get()
            dataentrada = entry3.get()
            datasaida = entry4.get()

            connection = hotel.cursor()

            values = (idcliente, idquarto, dataentrada, datasaida)

            try:

                connection.execute("INSERT INTO Reserva (IdCliente, IdQuarto, DataEntrada, DataSaida) "
                                   "VALUES (%s, %s, %s, %s)", values)

                hotel.commit()

                print(connection.rowcount, "Reserva gravado com sucesso!")

            except mysql.connector.Error as e:

                print(e)

        label = ttk.Label(self, text="Reservas", font=LARGEFONT)

        label.grid(row=0, column=4, padx=10, pady=10)

        text2 = ttk.Label(self, text="Insira o IdCliente")
        text2.grid(column=0, row=0, padx=10, pady=10)

        entry = ttk.Entry(self, width=45)
        entry.grid(column=0, row=1, padx=10, pady=10)

        text2 = ttk.Label(self, text="Insira o Id do Quarto")
        text2.grid(column=0, row=2, padx=10, pady=10)

        entry2 = ttk.Entry(self, width=45)
        entry2.grid(column=0, row=3, padx=10, pady=10)

        text3 = ttk.Label(self, text="Insira a data de entrada ex(2023-01-02)")
        text3.grid(column=0, row=4, padx=10, pady=10)

        entry3 = ttk.Entry(self, width=45)
        entry3.grid(column=0, row=5, padx=10, pady=10)

        text4 = ttk.Label(self, text="Insira a data de saida ex(2023-01-02)")
        text4.grid(column=0, row=6, padx=10, pady=10)

        entry4 = ttk.Entry(self, width=45)
        entry4.grid(column=0, row=7, padx=10, pady=10)

        button = ttk.Button(self, text="Registar", command=registarReserva)
        button.grid(row=8, column=0, padx=10, pady=10)

        button1 = ttk.Button(self, text="Clientes",
                             command=lambda: controller.show_frame(Page1))

        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Pagina Inicial",
                             command=lambda: controller.show_frame(StartPage))

        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Quartos",
                             command=lambda: controller.show_frame(Page2))

        button3.grid(row=3, column=1, padx=10, pady=10)


app = tkinterApp()
app.mainloop()
app.attributes('-fullscreen', True)
