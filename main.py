import mysql.connector

cinemas = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cinemas'
)

op = 1

while op != 0:
    op = str(input('Insira 1 para registar user: \n'
                   'Insira 2 para ver informações: \n'
                   'Insira 3 para apagar um registro: \n'
                   'Insira 4 para editar um registro: \nInsira 0 para '
                   'sair: \n'))

    if op == '1':
        Nome = str(input('insira o seu nome: \n'))

        Email = str(input('insira o seu email: \n'))

        Password = str(input('insira a sua Password: \n'))

        if Nome == '' or Email == '' or Password == '':
            print('não podem estar vazios')
        else:
            connection = cinemas.cursor()

            values = (Nome, Password, Email)

            connection.execute("INSERT INTO sala (descricao, pass, email) VALUES (%s, %s, %s)", values)

            cinemas.commit()

            if connection:
                print(connection.rowcount, "Registo inserido com sucesso!")
            else:
                print('Erro ao executar a query')
    elif op == '2':
        connection = cinemas.cursor()
        data = []
        connection.execute("SELECT * FROM sala")
        if connection:
            for x in connection:
                print(f"Nome: {x[1]} Email: {x[3]} Password: {x[2]}")
        else:
            print('Erro ao executar a query')
    elif op == '3':
        connection = cinemas.cursor()
        data = []
        connection.execute("SELECT * FROM sala")
        if connection:
            for x in connection:
                print(f"Id: {x[0]} Nome: {x[1]} Email: {x[3]} Password: {x[2]}")

            op2 = int(input('Insira o ID: \n'))

            connection2 = cinemas.cursor()

            connection2.execute(f"DELETE FROM sala WHERE id = {op2}")

            cinemas.commit()

            if connection2:
                print(connection2.rowcount, "Registo apagado com sucesso!")
            else:
                print('Erro ao executar a query')

        else:
            print('Erro ao executar a query')
    elif op == '4':
        connection = cinemas.cursor()

        connection.execute("SELECT * FROM sala")

        if connection:
            for x in connection:
                print(f"Id: {x[0]} Nome: {x[1]} Email: {x[3]} Password: {x[2]}")

            op2 = int(input('Insira o ID: \n'))

            Nome = str(input('insira o seu nome: \n'))

            Email = str(input('insira o seu email: \n'))

            Password = str(input('insira a sua Password: \n'))

            if Nome == '' or Email == '' or Password == '':
                print('não podem estar vazios')
            else:
                connection3 = cinemas.cursor()

                connection3.execute(f"UPDATE `sala` SET descricao='{Nome}', pass='{Email}', email='{Password}'"
                                    f"WHERE id = {op2}")

                cinemas.commit()

                if connection3:
                    print(connection.rowcount, "Registo editado com sucesso!")
                else:
                    print('Erro ao executar a query')

        else:
            print('Erro ao executar a query')
    elif op == '0':
        break
    else:
        print('Insira uma opção valida do menu!')
