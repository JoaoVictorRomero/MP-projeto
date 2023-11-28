from DAO.UsuarioDAO import UsuarioDAO
from DTO.Usuario import Usuario

# Teste de adição de usuário
def test_adicionar_usuario():
    usuario_dao = UsuarioDAO()
    usuario = Usuario(1, 'Usuário Teste', 'Função Teste', 'login_teste', 'senha_teste')
    resultado = usuario_dao.adicionar_usuario(usuario)
    assert resultado is True

# Teste de pesquisa de usuários
def test_pesquisar_usuarios():
    usuario_dao = UsuarioDAO()
    lista_usuarios = usuario_dao.pesquisar_usuarios()
    assert lista_usuarios is not None

# Teste de atualização de usuário
def test_atualizar_usuario():
    usuario_dao = UsuarioDAO()
    usuario = Usuario(1, 'Usuário Teste Atualizado', 'Nova Função', 'novo_login', 'nova_senha')
    resultado = usuario_dao.atualizar_usuario(usuario)
    assert resultado is True

# Teste de exclusão de usuário
def test_deletar_usuario():
    usuario_dao = UsuarioDAO()
    id_usuario = 1  # Defina o ID do usuário a ser excluído
    resultado = usuario_dao.deletar_usuario(id_usuario)
    assert resultado is True

def test_login_usuario():
    usuario_dao = UsuarioDAO()
    login = 'login_teste'
    senha = 'senha_teste'

    usuario_autenticado = usuario_dao.login_usuario(login, senha)

    assert usuario_autenticado is not None