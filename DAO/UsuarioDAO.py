import mysql.connector
from ConexaoBD import ConexaoBD
from Usuario import Usuario



class UsuarioDAO():
    '''Classe que define um Usuário do BD'''
    def adicionar_usuario(self, usuario: Usuario) -> bool:
        '''Função que adiciona um usuário ao BD'''
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            id_usuario = usuario.get_id_usuario()
            nome_usuario = usuario.get_nome_usuario()
            funcao = usuario.get_funcao()
            login = usuario.get_login()
            senha = usuario.get_senha()
            
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

    def pesquisar_usuarios(self) -> list:
        '''Função que retorna todos os usuário do BD'''
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
                id_usuario, nome_usuario, funcao, login, senha = linha
                
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

    def atualizar_usuario(self, usuario: Usuario) -> bool:
        '''Função que atualiza um usuário do BD com base no seu id'''
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            id_usuario = usuario.get_id_usuario()
            nome_usuario = usuario.get_nome_usuario()
            funcao = usuario.get_funcao()
            login = usuario.get_login()
            senha = usuario.get_senha()
            
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

    def deletar_usuario(self, id_usuario: int) -> bool:
        '''Função que remove um usuário do BD com base no seu id'''
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

    def login_usuario(self, login: str, senha: str) -> Usuario:
        '''Função que verifica as credenciais de um usuário do BD com base no seu login e senha'''
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            sql = 'SELECT * FROM usuarios WHERE login = %s AND senha = %s'

            cursor.execute(sql, (login, senha))
            resultado = cursor.fetchone()

            if resultado:
                id_usuario, nome_usuario, funcao, login_usuario, senha_usuario = resultado
                usuario = Usuario(id_usuario, nome_usuario, funcao, login_usuario, senha_usuario)

                print('Login realizado com sucesso!')

                return usuario

            else:
                print('Login ou senha inválidos!')

                return None

        except mysql.connector.Error as erro:
            print(f'UsuarioDAO - Pesquisar Usuários: {erro}')

            return None

        finally:
            cursor.close()
            conexao.desconecta_bd()
            