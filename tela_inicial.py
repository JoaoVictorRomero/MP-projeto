import PySimpleGUI as sg
from menu_de_busca import CRIAR_MENU

background_image = r"assets\background_4.png"

# Set the theme
sg.theme('Dark Blue 14')

# Create the main layout
main_layout = [
    [sg.Button("Sair",key="-SAIR-")],
    [sg.Image(filename=background_image,size=(6000,1000))],
]

# Create the main window
main = sg.Window("Food Finder", main_layout,finalize=True)
main.Maximize()
CRIAR_MENU()

# Event loop
while True:
    event, values = main.read()

    # Check if the window was closed
    if event == sg.WINDOW_CLOSED or event =="-SAIR-":
        break

# Close the window
main.close()
