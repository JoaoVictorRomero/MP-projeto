import PySimpleGUI as sg
from Usuario import Usuario
from UsuarioDAO import UsuarioDAO

sg.theme('dark blue 14')
logo_path = r'assets\logo_fundo.png'
def criar_tela_cadastro():
    cadastro_layout = [
        [sg.Button(key='-SAIR-', button_color=('#cd2323', sg.theme_background_color), size=(3, 3), button_text='Sair', font=('Arial', 30, 'bold'), border_width=0), 
        sg.Button(key='-BUSCAR-', button_color=('white', sg.theme_background_color), size=(10, 3), button_text='Buscar', font=('Arial', 35, 'bold'), border_width=0, ), 
        sg.Text('|', font=('Arial', 30, 'bold')), 
        sg.Button(key='-PRATO_DO_DIA-', button_color=('white', sg.theme_background_color), size=(10, 3), button_text='Pratos do dia', font=('Arial', 35, 'bold'), border_width=0), \
        sg.Text('|', font=('Arial', 30, 'bold')), 
        sg.Button(key='-MAPA-', button_color=('white', sg.theme_background_color), size=(10, 3), button_text='Mapa', font=('Arial', 35, 'bold'), border_width=0), 
        sg.Text(''), 
        sg.Text('|', font=('Arial', 30, 'bold')), 
        sg.Button(key='-LOGIN-', button_color=('gray', sg.theme_background_color), size=(10, 3), button_text='Login', font=('Arial', 30, 'bold'), border_width=0)], 
        [sg.Image(filename=logo_path, enable_events=True)], 
        [sg.Text('ID Usuário:', font=('Arial', 20, 'bold'), justification='center')],
        [sg.Input(key='id_usuario')], 
        [sg.Text('Nome do Usuário:', font=('Arial', 20, 'bold'), justification='center')],
        [sg.Input(key='nome_usuario')], 
        [sg.Text('Função:', font=('Arial', 20, 'bold'), justification='center')],
        [sg.Input(key='funcao')], 
        [sg.Text('Login:', font=('Arial', 20, 'bold'), justification='center')],
        [sg.Input(key='login')], 
        [sg.Text('Senha:', font=('Arial', 20, 'bold'), justification='center')],
        [sg.Input(key='senha')],
        [sg.Button(key='-CADASTRAR-', button_color=('#23cd4b', sg.theme_background_color), button_text='Cadastrar', font=('Arial', 30, 'bold'), border_width=0)], 
        [sg.Button(key='-LOGIN-', button_color=('#cd2323', sg.theme_background_color), button_text='Já tem cadastro? Faça login', font=('Arial', 20, 'bold'), border_width=0)]]
    
    menu_layout = sg.Window('Cadastro Usuário', cadastro_layout, finalize=True, element_justification='center')
    menu_layout.maximize()

    # Loop para interação com a janela
    while True:
        event, values = menu_layout.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        elif event == '-CADASTRAR-':
            id_usuario = int(values['id_usuario'])
            nome_usuario = values['nome_usuario']
            funcao = values['funcao']
            login = values['login']
            senha = values['senha']

            novo_usuario = Usuario(id_usuario, nome_usuario, funcao, login, senha)
            resultado = UsuarioDAO().adicionar_usuario(novo_usuario)

            print(resultado)

        elif event == '-LOGIN-':
            print('login')
        

        if event == '-SAIR-':
            for window in list(sg.Window()):
                sg.Window(window).close()