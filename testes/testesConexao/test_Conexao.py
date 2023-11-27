from conexao.conexao_bd import conexao_bd

def test_conecta_bd_sucesso():
    conexao = conexao_bd()
    resultado = conexao.conecta_bd()
    assert resultado is True  # Verifica se a conexão foi bem-sucedida

def test_conecta_bd_falha():
    # Simula um erro ao conectar alterando os dados de conexão
    conexao = conexao_bd()
    conexao.host = 'host_inexistente'  # Altera o host para forçar um erro de conexão
    resultado = conexao.conecta_bd()
    assert resultado is False  # Verifica se a conexão falhou

def test_desconecta_bd_sucesso():
    conexao = conexao_bd()
    conexao.conecta_bd()
    resultado = conexao.desconecta_bd()
    assert resultado is True  # Verifica se a desconexão foi bem-sucedida

def test_desconecta_bd_falha():
    # Simula uma desconexão falha ao fechar a conexão antes de estabelecer
    conexao = conexao_bd()
    resultado = conexao.desconecta_bd()
    assert resultado is False  # Verifica se a desconexão falhou