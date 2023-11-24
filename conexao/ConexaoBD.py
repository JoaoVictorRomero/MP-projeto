import mysql.connector

host = 'banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com'
user = 'doadmin'
password = 'AVNS_erI8p2wSSm0gckO83UU'
port = '25060'
database = 'defaultdb'

class ConexaoBD():
    def __init__(self):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.conn = self.conectaBD()
    
    def conectaBD(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )

            self.cursor = self.conn.cursor()

        except mysql.connector.Error as erro:
            print(f'ConexãoBD Conecta BD: {erro}')

        finally:
            self.desconectaBD()

    def desconectaBD(self):
        self.conn.close()

    def executaDQL(self, sql):
        try:
            self.conectaBD()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()

            return result

        except mysql.connector.Error as erro:
            print(f'ConexãoBD Executa DQL: {erro}')

        finally:
            self.desconectaBD()
    
    def executaDML(self, sql):
        try:
            self.conectaBD()
            self.cursor.execute(sql)
            result = self.cursor.commit()
        
        except mysql.connector.Error as erro:
            print(f'ConexãoBD Executa DML: {erro}')

        finally:
            self.desconectaBD()