from DTO.Usuario import Usuario

# Teste para verificar se a criação do usuário está funcionando corretamente
def test_criacao_usuario():
    usuario = Usuario(1, 'João', 'Admin', 'joao@example.com', 'senha123')
    assert usuario.get_id_usuario() == 1
    assert usuario.get_nome_usuario() == 'João'
    assert usuario.get_funcao() == 'Admin'
    assert usuario.get_login() == 'joao@example.com'
    assert usuario.get_senha() == 'senha123'

# Teste para verificar se a atualização do usuário está funcionando corretamente
def test_atualizacao_usuario():
    usuario = Usuario(1, 'João', 'Admin', 'joao@example.com', 'senha123')
    usuario.set_nome_usuario('José')
    usuario.set_funcao('Supervisor')
    usuario.set_login('jose@example.com')
    usuario.set_senha('novasenha456')
    
    assert usuario.get_nome_usuario() == 'José'
    assert usuario.get_funcao() == 'Supervisor'
    assert usuario.get_login() == 'jose@example.com'
    assert usuario.get_senha() == 'novasenha456'
