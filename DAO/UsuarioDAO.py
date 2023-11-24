from conexao import Conexao
from DTO import Usuario

class UsuarioDAO:
    def __init__(self):
        self.conexao = Conexao.getConexao()

    def adicionarUsuario(self, usuario):
        sql = 'INSERT INTO usuarios (id_usuario_ nome_usuario, funcao, login, senha) VALUES (%s, %s, %s, %s, %s)'

        try:
            cursor = self.conexao.cursor()

            cursor.execute(sql, (
                usuario.get_id_usuario(),
                usuario.get_nome_usuario(),
                usuario.get_funcao(),
                usuario.get_login(),
                usuario.get_senha()
            ))

            self.conexao.commit()

            print('Usuário adicionado com sucesso!')

        except mysql.connector.Error as erro:
            print('Erro ao adicionar usuário: {erro}')

usuario_dao = UsuarioDAO()

# Criando um objeto Usuário para adicionar
usuario_novo = Usuario(1, 'Marcelo Vitor', 'Admin', 'marcelovitor@gmail.com', '123')
usuario_dao.adicionarUsuario(usuario_novo)