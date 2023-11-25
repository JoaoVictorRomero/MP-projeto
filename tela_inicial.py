import PySimpleGUI as sg

menu_layout = [[sg.Text('O que vamos comer hoje?',font=('Arial',30,'bold'))],
               [sg.Input(key='-INPUT-')],
               [sg.Button('Buscar'),sg.Button('Não quero comer nada')]]

menu_principal = sg.Window('Food Finder',menu_layout,finalize=True)
menu_principal.Maximize()

while True:
    event,values = menu_principal.read()
    if event==sg.WINDOW_CLOSED or event=='Não quero comer nada':
        break

menu_principal.close()