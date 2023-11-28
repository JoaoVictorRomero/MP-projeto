from Pesquisa_Restaurante import Pesquisa_Restaurante

#Teste para verificar a inicialização da pesquisa por restaurante
def test_inicializacao_pesquisa_restaurante():
    pesquisa_restaurante = Pesquisa_Restaurante(1, 1, 1)
    assert pesquisa_restaurante.get_id_pesquisa_restaurante() == 1
    assert pesquisa_restaurante.get_fk_id_usuario() == 1
    assert pesquisa_restaurante.get_fk_id_restaurante() == 1

#Teste para verificar a atualização da pesquisa por restaurante
def test_atualizacao_pesquisa_restaurante():
    pesquisa_restaurante = Pesquisa_Restaurante(1, 1, 1)

    pesquisa_restaurante.set_id_pesquisa_restaurante(2)
    pesquisa_restaurante.set_fk_id_usuario(2)

    assert pesquisa_restaurante.get_id_pesquisa_restaurante() == 2
    assert pesquisa_restaurante.get_fk_id_usuario() == 2
    assert pesquisa_restaurante.get_fk_id_restaurante() == 1