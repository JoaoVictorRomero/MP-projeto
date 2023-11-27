import PySimpleGUI as sg
sg.theme('dark blue 14')
logo_path = r"assets\logo_fundo.png"
def criar_login():
    """Função que leva a criação do menu de login"""
    login_layout = [
                [sg.Button(key="-SAIR-",button_color=("#cd2323",sg.theme_background_color),size=(3,3),button_text="Sair",font=("Arial",30,'bold'),border_width=0),
                sg.Button(button_color=('white', sg.theme_background_color), border_width=0,size=(10,3),button_text="Buscar",font=("Arial",35,'bold'), key='-BUSCAR-'),\
                sg.Text('|',font=("Arial",30,'bold')), sg.Button(button_color=('white', sg.theme_background_color), border_width=0,size=(10,3),button_text="Pratos do dia",font=("Arial",35,'bold'), key='-PRATO_DO_DIA-'),\
                sg.Text('|',font=("Arial",30,'bold')), sg.Button(button_color=('white', sg.theme_background_color), border_width=0,size=(10,3),button_text="Mapa",font=("Arial",35,'bold'), key='-MAPA-'),sg.Text(''),
                sg.Text('|',font=("Arial",30,'bold')), sg.Button(button_color=('gray', sg.theme_background_color), border_width=0,size=(10,3),button_text="Login",font=("Arial",30,'bold'), key='-LOGIN-')],
                [sg.Image(filename=logo_path, enable_events=True)],
                [sg.Text('Nome de usuário',font=('Arial',20,'bold'),
                         justification='center')],
                [sg.Input(key='-USERNAME-')],
                [sg.Text('Senha',font=('Arial',20,'bold'),
                justification='center')],
                [sg.Input(key='-PASSWORD-',password_char='*')],
                [sg.Button(button_text="Entrar",font=("Arial",30,'bold'),button_color=('#23cd4b', sg.theme_background_color),border_width=0)],
                [sg.Button(button_text="Não tem login? Fazer cadastro!",font=("Arial",20,'bold'),button_color=('#cd2323', sg.theme_background_color),border_width=0)]]

    menu_login = sg.Window('Food Finder',login_layout,finalize=True,
                               element_justification='center')
    menu_login.maximize()
    while True:
        event,values = menu_login.read()
        if event==sg.WINDOW_CLOSED or event=='Não quero comer nada' or event=="-SAIR-":
            break
        if event=="-SAIR-":
            for window in sg.window_list():
                sg.Window(window).close()



