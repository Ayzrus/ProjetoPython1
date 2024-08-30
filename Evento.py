import mysql.connector

cinemas = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='evento'
)

op = 1

while op != 0:

    op = str(input('Insira 1 para registar evento: \n'
                   'Insira 2 para registar visitante: \n'
                   'Insira 3 para apagar um evento: \n'
                   'Insira 4 para editar um evento: \n'
                   'Insira 5 para apagar um visitante: \n'
                   'Insira 6 para editar um visitante: \n'
                   'Insira 7 para listar um evento: \n'
                   'Insira 8 para listar um visitante: \n'
                   'Insira 0 para '
                   'sair: \n'))

    if op == '1':

        descricao = str(input('Insira a descrição do evento: \n'))

        data = str(input('Insira a data do evento (yyyy-mm-dd): \n'))

        hora = str(input('Insira a hora do evento (hh:mm): \n'))

        if descricao == '' or data == '' or hora == '':

            print('não podem estar vazios')

        else:

            connection = cinemas.cursor()

            values = (descricao, data, hora)

            try:

                connection.execute("INSERT INTO evento (Descricao, Data, Hora) VALUES (%s, %s, %s)", values)

                cinemas.commit()

                print(connection.rowcount, "Record gravado com sucesso!")

            except mysql.connector.Error as e:

                print(e)

    elif op == '2':

        Nome = str(input('Insira o Nome do visitante: \n'))

        Nif = int(input('Insira o Nif do visitante: \n'))

        Email = str(input('Insira o Email do visitante: \n'))

        Id_Evento = int(input('Insira o Id do Evento: \n'))

        if Nome == '' or Nif == '' or Email == '' or Id_Evento == '':

            print('não podem estar vazios')

        else:

            connection = cinemas.cursor()

            values = (Nome, Nif, Email, Id_Evento)

            try:

                connection.execute(f"INSERT INTO visitante (Nome, Nif, Email, Id_Evento) VALUES "
                                   f"('{Nome}', {Nif}, '{Email}', {Id_Evento})")

                cinemas.commit()

                print(connection.rowcount, "Record gravado com sucesso!")

            except mysql.connector.Error as e:

                print(e)

    elif op == '3':

        connection = cinemas.cursor()

        try:

            connection.execute("SELECT * FROM evento")

            for x in connection:
                print(f"Id: {x[0]} Descrição: {x[1]} Data: {x[2]} Hora: {x[3]}")

            op2 = int(input('Insira o ID: \n'))

            connection2 = cinemas.cursor()

            try:
                connection2.execute(f"DELETE FROM evento WHERE Id = {op2}")

                cinemas.commit()

                print(connection2.rowcount, "Record apagado com sucesso!")

            except mysql.connector.Error as e:

                print(e)

        except mysql.connector.Error as e:

            print(e)

    elif op == '4':
        connection = cinemas.cursor()

        try:
            connection.execute("SELECT * FROM evento")

            for x in connection:
                print(f"Id: {x[0]} Descrição: {x[1]} Data: {x[2]} Hora: {x[3]}")

            op2 = int(input('Insira o ID: \n'))

            descricao = str(input('Insira a descrição do evento: \n'))

            data = str(input('Insira a data do evento (yyyy-mm-dd): \n'))

            hora = str(input('Insira a hora do evento (hh:mm): \n'))

            if descricao == '' or data == '' or hora == '':

                print('não podem estar vazios')

            else:

                try:

                    connection3 = cinemas.cursor()

                    connection3.execute(f"UPDATE evento "
                                        f"SET Descricao='{descricao}', Data='{data}', Hora='{hora}' WHERE Id = {op2}")

                    cinemas.commit()

                    print(connection.rowcount, "Record editado com sucesso!")

                except mysql.connector.Error as e:

                    print(e)

        except mysql.connector.Error as e:

            print(e)

    elif op == '5':

        connection = cinemas.cursor()

        try:

            connection.execute("SELECT * FROM visitante")

            for x in connection:
                print(f"Id: {x[0]} Nome: {x[1]} Nif: {x[2]} Email: {x[3]} Id_Evento: {x[3]}")

            op2 = int(input('Insira o ID: \n'))

            connection2 = cinemas.cursor()

            try:
                connection2.execute(f"DELETE FROM visitante WHERE Id = {op2}")

                cinemas.commit()

                print(connection2.rowcount, "Record apagado com sucesso!")

            except mysql.connector.Error as e:

                print(e)

        except mysql.connector.Error as e:

            print(e)

    elif op == '6':

        connection = cinemas.cursor()

        try:
            connection.execute("SELECT * FROM visitante")
            if connection == "":
                print('sem visitantes')
            else:
                for x in connection:
                    print(f"Id: {x[0]} Nome: {x[1]} Nif: {x[2]} Email: {x[3]} Id_Evento: {x[3]}")

                op2 = int(input('Insira o ID: \n'))

                Nome = str(input('Insira o Nome do visitante: \n'))

                Nif = int(input('Insira o Nif do visitante: \n'))

                Email = str(input('Insira o Email do visitante: \n'))

                Id_Evento = int(input('Insira o Id do Evento: \n'))

                if Nome == '' or Nif == '' or Email == '' or Id_Evento == '':

                    print('não podem estar vazios')

                else:

                    try:

                        connection3 = cinemas.cursor()

                        connection3.execute(f"UPDATE visitante "
                                            f"SET Nome='{Nome}',Nif='{Nif}',Email='{Email}',"
                                            f"Id_Evento='{Id_Evento}' WHERE Id = {op2}")

                        cinemas.commit()

                        print(connection.rowcount, "Record editado com sucesso!")

                    except mysql.connector.Error as e:

                        print(e)

        except mysql.connector.Error as e:

            print(e)
    elif op == '7':

        connection = cinemas.cursor()

        try:
            connection.execute("SELECT * FROM evento")
            if connection == "":
                print('sem eventos')
            else:
                for x in connection:
                    print(f"Id: {x[0]} Descrição: {x[1]} Data: {x[2]} Hora: {x[3]}")
        except mysql.connector.Error as e:

            print(e)
    elif op == '8':
        connection = cinemas.cursor()
        try:
            connection.execute("SELECT * FROM visitante")
            if connection == "":
                print('sem visitantes')
            else:
                for x in connection:
                    print(f"Id: {x[0]} Nome: {x[1]} Nif: {x[2]} Email: {x[3]} Id_Evento: {x[3]}")
        except mysql.connector.Error as e:

            print(e)
    elif op == '0':
        break
    else:
        print('Insira uma opção valida do menu!')
