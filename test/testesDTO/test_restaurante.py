from DTO.Restaurante import Restaurante

# Teste para verificar a inicialização do restaurante
def test_inicializacao_restaurante():
    restaurante = Restaurante(1, 'Restaurante A', 5)
    assert restaurante.get_id_restaurante() == 1
    assert restaurante.get_nome_restaurante() == 'Restaurante A'
    assert restaurante.get_distancia_totem() == 5

# Teste para verificar a atualização dos atributos do restaurante
def test_atualizacao_restaurante():
    restaurante = Restaurante(1, 'Restaurante A', 5)
    
    restaurante.set_nome_restaurante('Novo Restaurante')
    restaurante.set_distancia_totem(10)

    assert restaurante.get_nome_restaurante() == 'Novo Restaurante'
    assert restaurante.get_distancia_totem() == 10
