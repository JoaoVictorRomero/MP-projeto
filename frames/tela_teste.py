import sys
sys.path.append('./DAO')
sys.path.append('./DTO')

import PySimpleGUI as sg
from UsuarioDAO import UsuarioDAO
from Usuario import Usuario

# Layout da janela
layout = [
    [sg.Text('ID do Usuário'), sg.InputText(key='id_usuario')],
    [sg.Text('Nome do Usuário'), sg.InputText(key='nome_usuario')],
    [sg.Text('Função'), sg.InputText(key='funcao')],
    [sg.Text('Login'), sg.InputText(key='login')],
    [sg.Text('Senha'), sg.InputText(key='senha')],
    [sg.Button('Adicionar Usuário'), sg.Button('Cancelar')]
]

# Criando a janela
window = sg.Window('Adicionar Usuário', layout)

# Loop para interação com a janela
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    elif event == 'Adicionar Usuário':
        # Obter valores inseridos pelo usuário
        id_usuario = int(values['id_usuario'])
        nome_usuario = values['nome_usuario']
        funcao = values['funcao']
        login = values['login']
        senha = values['senha']

        # Criar objeto Usuario com os valores inseridos
        novo_usuario = Usuario(id_usuario, nome_usuario, funcao, login, senha)

        # Adicionar usuário ao banco de dados usando a função do DAO
        dao = UsuarioDAO()
        dao.adicionarUsuario(novo_usuario)
        sg.popup('Usuário adicionado com sucesso!')

window.close()