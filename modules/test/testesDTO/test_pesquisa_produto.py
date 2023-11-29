from Pesquisa_Produto import Pesquisa_Produto

def test_inicializacao_pesquisa_produto():
    '''Teste para verificar a inicialização da pesquisa por produto'''
    pesquisa_produto = Pesquisa_Produto(1, 1, 1)
    assert pesquisa_produto.get_id_pesquisa_produto() == 1
    assert pesquisa_produto.get_fk_id_usuario() == 1
    assert pesquisa_produto.get_fk_id_produto() == 1

def test_atualizacao_pesquisa_produto():
    '''Teste para verificar a atualização da pesquisa por produto'''
    pesquisa_produto = Pesquisa_Produto(1, 1, 1)

    pesquisa_produto.set_id_pesquisa_produto(2)
    pesquisa_produto.set_fk_id_usuario(2)

    assert pesquisa_produto.get_id_pesquisa_produto() == 2
    assert pesquisa_produto.get_fk_id_usuario() == 2
    assert pesquisa_produto.get_fk_id_produto() == 1