"""Framework que permite a criação de GUI nos python."""
import PySimpleGUI as sg
sg.theme('dark blue 14')
logo_path = r"assets\logo_fundo.png"
def criar_tela_pratos():
    """Função que leva a criação do menu de busca"""
    tela_pratos_do_dia_layout = [
                [sg.Button(key="-SAIR-",button_color=("#cd2323",sg.theme_background_color),size=(3,3),button_text="Sair",font=("Arial",30,'bold'),border_width=0),
                sg.Button(button_color=('white', sg.theme_background_color), border_width=0,size=(10,3),button_text="Buscar",font=("Arial",35,'bold'), key='-BUSCAR-'),\
                sg.Text('|',font=("Arial",30,'bold')), sg.Button(button_color=('#00d027', sg.theme_background_color), border_width=0,size=(10,3),button_text="Pratos do dia",font=("Arial",35,'bold'), key='-PRATO_DO_DIA-'),\
                sg.Text('|',font=("Arial",30,'bold')), sg.Button(button_color=('white', sg.theme_background_color), border_width=0,size=(10,3),button_text="Mapa",font=("Arial",35,'bold'), key='-MAPA-'),sg.Text(''),
                sg.Text('|',font=("Arial",30,'bold')), sg.Button(button_color=('gray', sg.theme_background_color), border_width=0,size=(10,3),button_text="Login",font=("Arial",30,'bold'), key='-LOGIN-')],
                [sg.Image(filename=logo_path, enable_events=True)],
                [sg.Text('Essas são as recomendações do dia!',font=('Arial',30,'bold'),
                         justification='center')],
                [sg.Button(button_text="Buscar",font=("Arial",30,'bold'),button_color=('#23cd4b', sg.theme_background_color),border_width=0),
                 sg.Button(button_text="Não quero comer nada",font=("Arial",20,'bold'),button_color=('#cd2323', sg.theme_background_color),border_width=0)]]

    tela_pratos_do_dia = sg.Window('Food Finder',tela_pratos_do_dia_layout,finalize=True,
                               element_justification='center')
    tela_pratos_do_dia.maximize()
    while True:
        event,values = tela_pratos_do_dia.read()
        if event==sg.WINDOW_CLOSED or event=='Não quero comer nada' or event=="-SAIR-":
            break
        if event=="-SAIR-":
            for window in list(sg.Window):
                sg.Window(window).close()
    tela_pratos_do_dia.close()