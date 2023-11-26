import PySimpleGUI as sg
from menu_de_busca import criar_menu
from menu_de_busca import logo_path
from menu_pratos_do_dia import criar_tela_pratos
from menu_mapa import criar_tela_mapa

background_image = r"assets\background_4.png"
logo_big_path = r"assets\logo_big.png"

# Set the theme
sg.theme_background_color="#21273d"

# Create the main layout
main_layout = [
    [sg.Button(key="-SAIR-",button_color=("#cd2323",sg.theme_background_color),size=(3,3),button_text="Sair",font=("Arial",30,'bold'),border_width=0),
    sg.Button(button_color=('white', sg.theme_background_color), border_width=0,size=(10,3),button_text="Buscar",font=("Arial",35,'bold'), key='-BUSCAR-'),\
    sg.Text('|',font=("Arial",30,'bold')), sg.Button(button_color=('white', sg.theme_background_color), border_width=0,size=(10,3),button_text="Pratos do dia",font=("Arial",35,'bold'), key='-PRATO_DO_DIA-'),\
    sg.Text('|',font=("Arial",30,'bold')), sg.Button(button_color=('white', sg.theme_background_color), border_width=0,size=(10,3),button_text="Mapa",font=("Arial",35,'bold'), key='-MAPA-'),sg.Text(''),
    sg.Text('|',font=("Arial",30,'bold')), sg.Button(button_color=('gray', sg.theme_background_color), border_width=0,size=(10,3),button_text="Login",font=("Arial",30,'bold'), key='-LOGIN-')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Text('')],
    [sg.Image(filename=logo_path)],
    [sg.Text("Food Finder",font=("Arial",60,"bold"))]
]

# Create the main window
main = sg.Window("Food Finder", main_layout,element_justification='center',finalize=True)
main.Maximize()

# Event loop
while True:
    event, values = main.read()

    # Check if the window was closed
    if event == sg.WINDOW_CLOSED or event =="-SAIR-":
        break
    if event == "-BUSCAR-":
        criar_menu()
    if event=='-PRATO_DO_DIA-':
        criar_tela_pratos()
    if event=='-MAPA-':
        criar_tela_mapa()

# Close the window
main.close()
