import sys
sys.path.append('./conexao')
sys.path.append('./DTO')

from ConexaoBD import ConexaoBD
from Usuario import Usuario

import mysql.connector

class UsuarioDAO:
    def __init__(self):
        conn = ConexaoBD(
            host='banco-de-dados-mp-do-user-15247043-0.c.db.ondigitalocean.com',
            user='doadmin',
            password='AVNS_erI8p2wSSm0gckO83UU',
            port='25060',
            database='defaultdb'
        )
        
        self.conexao = conn.conectaBD()

    def adicionarUsuario(self, usuario):
        
        if self.conexao:
            sql = 'INSERT INTO usuarios (nome_usuario, funcao, login, senha) VALUES (%s, %s, %s, %s)'

            try:
                cursor = self.conexao.cursor()

                cursor.execute(sql, (
                    usuario.get_nome_usuario(),
                    usuario.get_funcao(),
                    usuario.get_login(),
                    usuario.get_senha()
                ))

                self.conexao.commit()
                print('Usuário adicionado com sucesso!')

            except mysql.connector.Error as erro:
                print(f'Erro ao adicionar usuário: {erro}')

        else:
            print('Conexão não estabelecida. Não foi possível adicionar o usuário.')

usuario_dao = UsuarioDAO()

# Criando um objeto Usuário para adicionar
usuario_novo = Usuario('Marcelo Vitor', 'Admin', 'marcelovitor@gmail.com', '123')
usuario_dao.adicionarUsuario(usuario_novo)