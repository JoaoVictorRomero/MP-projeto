from menu_de_busca import test_criar_menu

def test_tela_menu():
    resultado = test_criar_menu()

    assert resultado == 0
