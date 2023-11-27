from DTO.Usuario import Usuario

def test_criar_usuario():
    novo_usuario = Usuario(id_usuario=1, nome_usuario='Teste', funcao='Teste', login='teste@gmail.com', senha='senha')

    assert novo_usuario.getNome_usuario() == 'Teste'