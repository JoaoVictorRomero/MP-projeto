from DTO.Produto import Produto

def test_inicializacao_produto():
    '''Teste para verificar a inicialização do produto'''
    produto = Produto(1, 'Produto A', 1)
    assert produto.get_id_produto() == 1
    assert produto.get_nome_produto() == 'Produto A'
    assert produto.get_fk_id_restaurante() == 1

def test_atualizacao_produto():
    '''Teste para verificar a atualização dos atributos do produto'''
    produto = Produto(1, 'Produto A', 1)
    
    produto.set_nome_produto('Novo Produto')
    produto.set_fk_id_restaurante(2)

    assert produto.get_nome_produto() == 'Novo Produto'
    assert produto.get_fk_id_restaurante() == 2
    