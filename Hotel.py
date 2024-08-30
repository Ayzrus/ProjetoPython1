import mysql.connector
import os

hotel = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='hotel'
)


def registarCliente():
    os.system('cls')
    nif = int(input('Insira o nif: \n'))

    nome = str(input('Insira o nome: \n'))

    morada = str(input('Insira a morada: \n'))

    telefone = int(input('Insira o telefone: \n'))

    email = str(input('Insira o email: \n'))

    cc = str(input('Insira o cc: \n'))

    os.system('cls')

    if nif == "" or nome == "" or morada == "" or telefone == "" or email == "" or cc == "":
        print("Os Campos não podem estar vazios")
        pass
    else:
        connection = hotel.cursor()

        values = (nif, nome, morada, telefone, email, cc)

        try:

            connection.execute("INSERT INTO Cliente (Nif, Nome, Morada, Telefone, Email, CC) "
                               "VALUES (%s, %s, %s, %s, %s, %s)", values)

            hotel.commit()

            print(connection.rowcount, "Cliente gravado com sucesso!")

        except mysql.connector.Error as e:

            print(e)


def registarQuarto():
    os.system('cls')
    connection = hotel.cursor()

    try:

        connection.execute("SELECT * FROM Tipo")

        for x in connection:
            print(x)

        nquarto = int(input('Insira o número do quarto: \n'))

        idtipo = int(input('Insira o id do tipo: \n'))

        os.system('cls')

        if nquarto == "" or idtipo == "":
            print("Os Campos não podem estar vazios")
            pass
        else:
            connection2 = hotel.cursor()

            values = (nquarto, idtipo)

            try:

                connection2.execute("INSERT INTO Quarto (Numero, Id_Tipo) VALUES (%s, %s)", values)

                hotel.commit()

                print(connection2.rowcount, "Quarto gravado com sucesso!")

            except mysql.connector.Error as e:

                print(e)

    except mysql.connector.Error as e:

        print(e)


def registarReserva():
    os.system('cls')
    connection = hotel.cursor()

    try:

        connection.execute("SELECT * FROM Cliente")

        for x in connection:
            print(f"Nif: {x[0]} Nome: {x[1]}")

        connection2 = hotel.cursor()

        try:

            connection2.execute("SELECT * FROM Quarto")

            for c in connection2:
                print(f"Id: {c[0]} Numero do Quarto: {c[1]}")

            idcliente = int(input('Insira o id do cliente: \n'))

            idquarto = int(input('Insira o id do quarto: \n'))

            dataentrada = str(input('Insira a data de entrada ex: (2023-01-18): \n'))

            datasaida = str(input('Insira a data de saida ex: (2023-01-18): \n'))

            os.system('cls')

            if idcliente == "" or idquarto == "" or dataentrada == "" or datasaida == "":
                print("Os Campos não podem estar vazios")
                pass
            else:
                connection3 = hotel.cursor()

                values = (idcliente, idquarto, dataentrada, datasaida)

                try:

                    connection3.execute("INSERT INTO Reserva (IdCliente, IdQuarto, DataEntrada, DataSaida) "
                                        "VALUES (%s, %s, %s, %s)", values)

                    hotel.commit()

                    print(connection3.rowcount, "Reserva gravada com sucesso!")

                except mysql.connector.Error as e:

                    print(e)

        except mysql.connector.Error as e:

            print(e)

    except mysql.connector.Error as e:

        print(e)


def listarReserva():
    os.system('cls')
    connection = hotel.cursor()

    try:

        connection.execute("SELECT R.Id, C.Nome, Q.Numero,R.DataEntrada, R.DataSaida FROM Reserva R "
                           "LEFT JOIN Cliente C ON C.Nif = R.IdCliente \n"
                           "LEFT JOIN Quarto Q ON Q.Id = R.IdQuarto")

        for x in connection:
            print(f"Id: {x[0]} Nome Cliente: {x[1]} Numero Quarto: {x[2]} Data Entrada: {x[3]} Data Saida: {x[4]}")

    except mysql.connector.Error as e:

        print(e)


def editarCliente():
    os.system('cls')
    connection = hotel.cursor()

    try:

        connection.execute("SELECT * FROM Cliente")

        for x in connection:
            print(f"Nif: {x[0]} Nome: {x[1]} Morada: {x[2]} Telefone: {x[3]} Email: {x[4]} CC: {x[5]}")

        nifcliente = int(input('Insira o nif do cliente: \n'))

        nif = int(input('Insira o nif: \n'))

        nome = str(input('Insira o nome: \n'))

        morada = str(input('Insira a morada: \n'))

        telefone = int(input('Insira o telefone: \n'))

        email = str(input('Insira o email: \n'))

        cc = str(input('Insira o cc: \n'))

        os.system('cls')

        if nif == "" or nome == "" or morada == "" or telefone == "" or email == "" or cc == "":
            print("Os Campos não podem estar vazios")
            pass
        else:
            connection2 = hotel.cursor()

            try:

                connection2.execute(f"UPDATE cliente SET Nif='{nif}', Nome='{nome}', Morada='{morada}', "
                                    f"Telefone='{telefone}', Email='{email}', CC='{cc}' WHERE Nif = '{nifcliente}'")

                hotel.commit()

                print(connection2.rowcount, "Cliente Editado com sucesso!")

            except mysql.connector.Error as e:

                print(e)

    except mysql.connector.Error as e:

        print(e)


def listarReservaPorQuarto():
    os.system('cls')
    connection = hotel.cursor()

    try:

        connection.execute("SELECT R.Id, C.Nome, Q.Numero,R.DataEntrada, R.DataSaida, R.IdQuarto FROM Reserva R "
                           "LEFT JOIN Cliente C ON C.Nif = R.IdCliente \n"
                           "LEFT JOIN Quarto Q ON Q.Id = R.IdQuarto")

        for x in connection:
            print(f"Id: {x[0]} Nome Cliente: {x[1]} Numero Quarto: {x[2]} Data Entrada: {x[3]} Data Saida: {x[4]} "
                  f"Id do Quarto: {x[5]}")

        idQuarto = int(input('Insira o id do quarto: \n'))

        os.system('cls')

        if idQuarto == "":
            print("Os Campos não podem estar vazios")
            pass
        else:
            connection2 = hotel.cursor()

            try:

                connection2.execute("SELECT R.Id, C.Nome, Q.Numero,R.DataEntrada, R.DataSaida FROM Reserva R "
                                    "LEFT JOIN Cliente C ON C.Nif = R.IdCliente \n"
                                    "LEFT JOIN Quarto Q ON Q.Id = R.IdQuarto \n"
                                    f"WHERE R.IdQuarto = '{idQuarto}'")

                for x in connection2:
                    print(
                        f"Id: {x[0]} Nome Cliente: {x[1]} Numero Quarto: {x[2]} Data Entrada: {x[3]} "
                        f"Data Saida: {x[4]}")

            except mysql.connector.Error as e:

                print(e)

    except mysql.connector.Error as e:

        print(e)


def listarReservaPorDataEntrada():
    os.system('cls')
    connection = hotel.cursor()

    try:

        connection.execute("SELECT R.Id, C.Nome, Q.Numero,R.DataEntrada, R.DataSaida FROM Reserva R "
                           "LEFT JOIN Cliente C ON C.Nif = R.IdCliente \n"
                           "LEFT JOIN Quarto Q ON Q.Id = R.IdQuarto")

        for x in connection:
            print(f"Id: {x[0]} Nome Cliente: {x[1]} Numero Quarto: {x[2]} Data Entrada: {x[3]} Data Saida: {x[4]} ")

        dataReserva = str(input('Insira a data de entrada da reserva: \n'))

        os.system('cls')

        if dataReserva == "":
            print("Os Campos não podem estar vazios")
            pass
        else:
            connection2 = hotel.cursor()

            try:

                connection2.execute("SELECT R.Id, C.Nome, Q.Numero,R.DataEntrada, R.DataSaida FROM Reserva R "
                                    "LEFT JOIN Cliente C ON C.Nif = R.IdCliente \n"
                                    "LEFT JOIN Quarto Q ON Q.Id = R.IdQuarto \n"
                                    f"WHERE R.DataEntrada = '{dataReserva}'")

                for x in connection2:
                    print(
                        f"Id: {x[0]} Nome Cliente: {x[1]} Numero Quarto: {x[2]} Data Entrada: {x[3]} "
                        f"Data Saida: {x[4]}")

            except mysql.connector.Error as e:

                print(e)

    except mysql.connector.Error as e:

        print(e)


op = 1

while op != 0:

    op = str(input('Insira 1 para registar um quarto: \n'
                   'Insira 2 para registar um cliente: \n'
                   'Insira 3 para registar uma reserva: \n'
                   'Insira 4 para listar reservas: \n'
                   'Insira 5 para editar cliente: \n'
                   'Insira 6 para listar reservas de um quarto: \n'
                   'Insira 7 para listar reservas de uma data: \n'
                   'Insira 8 para sair: \n'))

    if op == '1':
        registarQuarto()
    elif op == '2':
        registarCliente()
    elif op == '3':
        registarReserva()
    elif op == '4':
        listarReserva()
    elif op == '5':
        editarCliente()
    elif op == '6':
        listarReservaPorQuarto()
    elif op == '7':
        listarReservaPorDataEntrada()
    elif op == '8':
        break
    else:
        print('Insira uma opção valida do menu!')
