import mysql.connector

conexao = mysql.connector.connect(
    host = 'banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com',
    user = 'doadmin',
    password = 'AVNS_erI8p2wSSm0gckO83UU',
    port = '25060',
    database = 'defaultdb'
)

if conexao.is_connected():
    print('Sucesso!')

conexao.close()