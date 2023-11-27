from DTO.Usuario import Usuario

# Teste para verificar se a criação do usuário está funcionando corretamente
def test_criacao_usuario():
    usuario = Usuario(1, 'João', 'Admin', 'joao@example.com', 'senha123')
    assert usuario.getId_usuario() == 1
    assert usuario.getNome_usuario() == 'João'
    assert usuario.getFuncao() == 'Admin'
    assert usuario.getLogin() == 'joao@example.com'
    assert usuario.getSenha() == 'senha123'

# Teste para verificar se a atualização do usuário está funcionando corretamente
def test_atualizacao_usuario():
    usuario = Usuario(1, 'João', 'Admin', 'joao@example.com', 'senha123')
    usuario.setNome_usuario('José')
    usuario.setFuncao('Supervisor')
    usuario.setLogin('jose@example.com')
    usuario.setSenha('novasenha456')
    
    assert usuario.getNome_usuario() == 'José'
    assert usuario.getFuncao() == 'Supervisor'
    assert usuario.getLogin() == 'jose@example.com'
    assert usuario.getSenha() == 'novasenha456'
