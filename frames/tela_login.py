import sys
sys.path.append('DAO')
sys.path.append('DTO')

import PySimpleGUI as sg
from UsuarioDAO import UsuarioDAO
from Usuario import Usuario

# Layout da janela
layout = [
    [sg.Text('Login'), sg.InputText(key='login')],
    [sg.Text('Senha'), sg.InputText(key='senha')],
    [sg.Button('Login', key='LOGIN'), sg.Button('Cancelar')]
]

# Criando a janela
window = sg.Window('Login Usuário', layout)

# Loop para interação com a janela
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    elif event == 'LOGIN':
        # Obter valores inseridos pelo usuário
        login = values['login']
        senha = values['senha']

        # Adicionar usuário ao banco de dados usando a função do DAO
        resultado = UsuarioDAO.login_usuario(login, senha)
        print(resultado)

        sg.popup('Usuário adicionado com sucesso!')

window.close()