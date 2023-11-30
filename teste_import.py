import sys
sys.path.append('./MP-projeto')

from DTO.Classe_Usuario import Usuario

usuario_novo = Usuario(1, 'Teste', 'Função', 'login', 'senha')

print(usuario_novo)