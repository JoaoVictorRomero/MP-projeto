import sys
sys.path.append('./conexao')
sys.path.append('./DTO')

from ConexaoBD import ConexaoBD
from Usuario import Usuario

import mysql.connector

class UsuarioDAO():
    def adicionarUsuario(self, usuario):
        conexao = ConexaoBD()
        conexao.conectaBD()

        try:
            conn = conexao.conn #Obtém a conexão
            cursor = conn.cursor()

            id_usuario = usuario.getId_usuario()
            nome_usuario = usuario.getNome_usuario()
            funcao = usuario.getFuncao()
            login = usuario.getLogin()
            senha = usuario.getSenha()
            
            sql = 'INSERT INTO usuarios (id_usuario, nome_usuario, funcao, login, senha) VALUES (%s, %s, %s, %s, %s)'

            cursor.execute(sql, (id_usuario, nome_usuario, funcao, login, senha))
            conn.commit()
            print('Usuário adicionado com sucesso!')

        except mysql.connector.Error as erro:
            print(f'UsuarioDAO - Adicionar Usuário: {erro}')

        finally:
            cursor.close()
            conexao.desconectaBD()

    def pesquisarUsuarios(self):
        conexao = ConexaoBD()
        conexao.conectaBD()

        try:
            conn = conexao.conn #Obtém a conexão
            cursor = conn.cursor()

            sql = 'SELECT * FROM usuarios'

            cursor.execute(sql)
            resultado = cursor.fetchall()

            for linha in resultado:
                print(linha)

            print('Usuários listados com sucesso!')

        except mysql.connector.Error as erro:
            print(f'UsuarioDAO - Pesquisar Usuários: {erro}')

        finally:
            cursor.close()
            conexao.desconectaBD()

print(UsuarioDAO().pesquisarUsuarios())