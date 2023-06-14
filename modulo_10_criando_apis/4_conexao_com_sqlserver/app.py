import os
import pyodbc
from dotenv import load_dotenv

load_dotenv('.env')

class DbConnection():
    server = os.environ.get('SERVER')
    database = os.environ.get('DATABASE')
    username = os.environ.get('USER')
    password = os.environ.get('PASS')

    def connect_db(self):
        try:

            cnx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+DbConnection.server+';DATABASE='+DbConnection.database+';UID='+DbConnection.username+';PWD='+ DbConnection.password)

            return cnx

        except pyodbc.Error as error:
            print(f'Ocorreu um erro na conexão com o banco de dados: {error}')

    def disconnect_db(self, cnx):
        try:
            cnx.close()
        except pyodbc.Error as error:
            print(f'Ocorreu um erro ao tentar desconectar o banco de dados: {error}')

    def list_users(self, cnx):
        cursor = cnx.cursor()
        usuarios = cursor.execute('select * from users')
        for usuario in usuarios:
            print(usuario)

lista = DbConnection()
print(lista.list_users(lista.connect_db()))