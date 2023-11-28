from Pesquisa_Restaurante import Pesquisa_Restaurante

def test_criacao_pesquisa_restaurante():
    pesquisa_restaurante = Pesquisa_Restaurante(1, 1, 1)
    assert pesquisa_restaurante.get_id_pesquisa_restaurante == 1
    assert pesquisa_restaurante.get_fk_id_usuario== 1
    assert pesquisa_restaurante.get_fk_id_restaurante == 1