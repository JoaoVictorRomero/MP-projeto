from DAO.RestauranteDAO import RestauranteDAO
from DTO.Restaurante import Restaurante

# Teste de adição de restaurante
def test_adicionar_restaurante():
    restaurante_dao = RestauranteDAO()
    restaurante = Restaurante(1, 'Restaurante Teste', 50.35)
    resultado = restaurante_dao.adicionar_restaurante(restaurante)
    assert resultado is True

def test_pesquisar_restaurantes():
    restaurante_dao = RestauranteDAO()
    lista_restaurantes = restaurante_dao.pesquisar_restaurantes()
    assert lista_restaurantes is not None

def test_atualizar_restaurante():
    restaurante_dao = RestauranteDAO()
    restaurante = Restaurante(1, 'Restaurante Teste Atualizado', 50.35)
    resultado = restaurante_dao.atualizar_restaurante(restaurante)
    assert resultado is True

def test_deletar_restaurante():
    restaurante_dao = RestauranteDAO()
    id_restaurante = 2  # Defina o ID do restaurante a ser excluído
    resultado = restaurante_dao.deletar_restaurante(id_restaurante)
    assert resultado is True