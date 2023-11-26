import PySimpleGUI as sg
def CRIAR_MENU():    
    sg.theme('dark blue 14')
    logo_path = "assets\logo_fundo.png"
    menu_layout = [[sg.Image(filename=logo_path, enable_events=True)],
                [sg.Text('O que vamos comer hoje?',font=('Arial',30,'bold'),justification='center')],
                [sg.Input(key='-INPUT-')],
                [sg.Button('Buscar'),sg.Button('Não quero comer nada')]]

    menu_principal = sg.Window('Food Finder',menu_layout,finalize=True,element_justification='center')

    while True:
        event,values = menu_principal.read()
        if event==sg.WINDOW_CLOSED or event=='Não quero comer nada':
            break

    menu_principal.close()

def TEST_CRIAR_MENU():    
    sg.theme('dark blue 14')
    logo_path = "assets\logo_fundo.png"
    menu_layout = [[sg.Image(filename=logo_path, enable_events=True)],
                [sg.Text('O que vamos comer hoje?',font=('Arial',30,'bold'),justification='center')],
                [sg.Input(key='-INPUT-')],
                [sg.Button('Buscar'),sg.Button('Não quero comer nada')]]

    menu_principal = sg.Window('Food Finder',menu_layout,finalize=True,element_justification='center')
    menu_principal.close()
    return 0