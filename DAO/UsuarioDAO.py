import sys
sys.path.append('/.conexao')
sys.path.append('/.DTO')

from conexao.ConexaoBD import ConexaoBD
from DTO.Usuario import Usuario
import mysql.connector


class UsuarioDAO():
    def adicionar_usuario(self, usuario):
        conexao = ConexaoBD()
        conexao.conecta_bd()

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

            return True

        except mysql.connector.Error as erro:
            print(f'UsuarioDAO - Adicionar Usuário: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def pesquisar_usuarios(self):
        conexao = ConexaoBD()
        conexao.conecta_bd()

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
            conexao.desconecta_bd()

    def atualizar_usuario(self, usuario):
        conexao = ConexaoBD()
        conexao.conecta_bd()

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

            return True

        except mysql.connector.Error as erro:
            print(f'UsuarioDAO - Atualizar Usuário: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def deletar_usuario(self, id_usuario):
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            sql = 'DELETE FROM usuarios WHERE id_usuario = %s'

            cursor.execute(sql, (id_usuario,))
            conn.commit()
            print('Usuário excluído com sucesso!')

            return True

        except mysql.connector.Error as erro:
            print(f'UsuarioDAO - Deletar Usuário: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def login_usuario(self):
        conexao = ConexaoBD()
        conexao.conecta_bd()

        listaUsuarios = list()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            sql = 'SELECT id_usuario FROM usuarios WHERE login = %s AND senha = %s'

            cursor.execute(sql)
            id_usuario = cursor.fetchall()

            print('Usuários listados com sucesso!')
            
            return id_usuario

        except mysql.connector.Error as erro:
            print(f'UsuarioDAO - Pesquisar Usuários: {erro}')
            return -1

        finally:
            cursor.close()
            conexao.desconecta_bd()