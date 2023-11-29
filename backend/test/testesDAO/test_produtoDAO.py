from DAO.ProdutoDAO import ProdutoDAO
from DTO.Produto import Produto

# Teste de adição de produto
def test_adicionar_produto():
    produto_dao = ProdutoDAO()
    produto = Produto(1, 'Produto Teste', 1)
    resultado = produto_dao.adicionar_produto(produto)
    assert resultado is True

# Teste de pesquisa de produtos
def test_pesquisar_produtos():
    produto_dao = ProdutoDAO()
    lista_produtos = produto_dao.pesquisar_produtos()
    assert lista_produtos is not None

# Teste de atualização de produto
def test_atualizar_produto():
    produto_dao = ProdutoDAO()
    produto = Produto(1, 'Produto Teste Atualizado', 1)
    resultado = produto_dao.atualizar_produto(produto)
    assert resultado is True

# Teste de exclusão de produto
def test_deletar_produto():
    produto_dao = ProdutoDAO()
    id_produto = 1  # Defina o ID do produto a ser excluído
    resultado = produto_dao.deletar_produto(id_produto)
    assert resultado is True
