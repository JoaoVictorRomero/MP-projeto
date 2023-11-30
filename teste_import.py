import sys
sys.path.append('../backend')

from DTO.classe_usuario import Usuario

usuario_novo = Usuario(1, 'Teste', 'Função', 'login', 'senha')

print(usuario_novo)