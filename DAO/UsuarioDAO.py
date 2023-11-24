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
            conn = conexao.conn #Obtém a conexão com o BD
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

        listaUsuarios = list()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            sql = 'SELECT * FROM usuarios'

            cursor.execute(sql)
            resultado = cursor.fetchall()

            for linha in resultado:
                id_usuario = linha[0]
                nome_usuario = linha[1]
                funcao = linha[2]
                login = linha[3]
                senha = linha[4]
                
                usuario = Usuario(id_usuario, nome_usuario, funcao, login, senha)

                listaUsuarios.append(usuario)

            print('Usuários listados com sucesso!')
            
            return listaUsuarios

        except mysql.connector.Error as erro:
            print(f'UsuarioDAO - Pesquisar Usuários: {erro}')
            return []

        finally:
            cursor.close()
            conexao.desconectaBD()

    def atualizarUsuario(self, usuario):
        conexao = ConexaoBD()
        conexao.conectaBD()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            id_usuario = usuario.getId_usuario()
            nome_usuario = usuario.getNome_usuario()
            funcao = usuario.getFuncao()
            login = usuario.getLogin()
            senha = usuario.getSenha()
            
            sql = 'UPDATE usuarios SET nome_usuario = %s, funcao = %s, login = %s, senha = %s WHERE id_usuario = %s'

            cursor.execute(sql, (nome_usuario, funcao, login, senha, id_usuario))
            conn.commit()
            print('Usuário atualizado com sucesso!')

        except mysql.connector.Error as erro:
            print(f'UsuarioDAO - Atualizar Usuário: {erro}')

        finally:
            cursor.close()
            conexao.desconectaBD()

usuario = Usuario(1, 'Marcelo', 'Ad', 'marcelo', '123')
UsuarioDAO().atualizarUsuario(usuario)