import sys
sys.path.append('./modules')

import DTO
usuario_novo = DTO.Classe_Usuario.Usuario(1, 'Teste', 'Função', 'login', 'senha')

print(usuario_novo)