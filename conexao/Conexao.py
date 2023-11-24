import mysql.connector

host = 'banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com'
user = 'doadmin'
password = 'AVNS_erI8p2wSSm0gckO83UU'
port = '25060'
database = 'defaultdb'

class Conexao:
    def __init__(self):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.conn = self.getConexao()
    
    def getConexao():
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database
        )