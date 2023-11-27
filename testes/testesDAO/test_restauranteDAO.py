from DAO.RestauranteDAO import RestauranteDAO
from DTO.Restaurante import Restaurante

# Teste de adição de restaurante
def test_adicionar_restaurante():
    restaurante_dao = RestauranteDAO()
    restaurante = Restaurante(1, 'Restaurante Teste', 50.35)
    resultado = restaurante_dao.adicionar_restaurante(restaurante)
    assert resultado is True
    