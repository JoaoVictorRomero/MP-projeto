import PySimpleGUI as sg
from menu_de_busca import criar_menu
from menu_de_busca import logo_path
from menu_pratos_do_dia import criar_tela_pratos
from menu_mapa import criar_tela_mapa
from menu_login import criar_login
from menu_cadastro import criar_tela_cadastro

background_image = r'assets\background_4.png'
logo_big_path = r'assets\logo_big.png'

# Set the theme
sg.theme_background_color='#21273d'

# Create the main layout
main_layout = [
    [sg.Button(key='-SAIR-', button_color=('#cd2323', sg.theme_background_color), size=(3, 3), button_text='Sair', font=('Arial', 30, 'bold'), border_width=0), 
    sg.Button(key='-BUSCAR-', button_color=('white', sg.theme_background_color), size=(10, 3), button_text='Buscar', font=('Arial', 35, 'bold'), border_width=0), 
    sg.Text('|', font=('Arial', 30, 'bold')), 
    sg.Button(key='-PRATO_DO_DIA-', button_color=('white', sg.theme_background_color), size=(10, 3), button_text='Pratos do dia', font=('Arial', 35, 'bold'), border_width=0), 
    sg.Text('|', font=('Arial', 30, 'bold')), 
    sg.Button(key='-MAPA-', button_color=('white', sg.theme_background_color), size=(10, 3), button_text='Mapa', font=('Arial', 35, 'bold'), border_width=0), 
    sg.Text(''), 
    sg.Text('|', font=('Arial', 30, 'bold')), 
    sg.Button(key='-LOGIN-', button_color=('gray', sg.theme_background_color), size=(10, 3), button_text='Login', font=('Arial', 30, 'bold'), border_width=0), 
    sg.Text('|', font=('Arial', 30, 'bold')), 
    sg.Button(key='-CADASTRAR-', button_color=('gray', sg.theme_background_color), size=(10, 3), button_text='Cadastrar', font=('Arial', 30, 'bold'), border_width=0)], 
    [sg.Text('')], 
    [sg.Text('')], 
    [sg.Text('')], 
    [sg.Text('')], 
    [sg.Image(filename=logo_path)], 
    [sg.Text('Food Finder', font=('Arial', 60, 'bold'))]
]

# Create the main window
main = sg.Window('Food Finder', main_layout, element_justification='center', finalize=True)
main.Maximize()

# Event loop
while True:
    event, values = main.read()

    # Check if the window was closed
    if event == sg.WINDOW_CLOSED or event =='-SAIR-':
        break
    if event == '-BUSCAR-':
        criar_menu()
    if event == '-PRATO_DO_DIA-':
        criar_tela_pratos()
    if event == '-MAPA-':
        criar_tela_mapa()
    if event == '-LOGIN-':
        criar_login()
    if event == '-CADASTRAR-':
        criar_tela_cadastro()

# Close the window
main.close()
