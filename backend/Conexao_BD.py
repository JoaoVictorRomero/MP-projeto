import mysql.connector

host = 'banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com'
user = 'doadmin'
password = 'AVNS_erI8p2wSSm0gckO83UU'
port = '25060'
database = 'defaultdb'

class ConexaoBD:
    def __init__(self):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.conn = None
        self.cursor = None
    
    def conecta_bd(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )

            self.cursor = self.conn.cursor()

            return True

        except mysql.connector.Error as erro:
            print(f'ConexãoBD - Conecta BD: {erro}')
            
            return False

    def desconecta_bd(self):
        try:
            if self.conn and self.conn.is_connected():
                if self.cursor:
                    self.cursor.close()

                self.conn.close()

                return True

        except mysql.connector.Error as erro:
            print(f'ConexãoBD - Desconecta BD: {erro}')

        return False