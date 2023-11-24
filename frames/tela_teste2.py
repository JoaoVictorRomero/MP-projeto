import sys
sys.path.append('./DAO')
sys.path.append('./DTO')

import tkinter as tk
from UsuarioDAO import UsuarioDAO
from Usuario import Usuario

def adicionar_usuario():
    id_usuario = int(entry_id.get())
    nome_usuario = entry_nome.get()
    funcao = entry_funcao.get()
    login = entry_login.get()
    senha = entry_senha.get()

    novo_usuario = Usuario(id_usuario, nome_usuario, funcao, login, senha)

    dao = UsuarioDAO()
    dao.adicionarUsuario(novo_usuario)

    label_status.config(text='Usuário adicionado com sucesso!')

root = tk.Tk()
root.title('Adicionar Usuário')

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_id = tk.Label(frame, text='ID do Usuário:')
label_id.grid(row=0, column=0)
entry_id = tk.Entry(frame)
entry_id.grid(row=0, column=1)

label_nome = tk.Label(frame, text='Nome do Usuário:')
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=1, column=1)

label_funcao = tk.Label(frame, text='Função:')
label_funcao.grid(row=2, column=0)
entry_funcao = tk.Entry(frame)
entry_funcao.grid(row=2, column=1)

label_login = tk.Label(frame, text='Login:')
label_login.grid(row=3, column=0)
entry_login = tk.Entry(frame)
entry_login.grid(row=3, column=1)

label_senha = tk.Label(frame, text='Senha:')
label_senha.grid(row=4, column=0)
entry_senha = tk.Entry(frame)
entry_senha.grid(row=4, column=1)

button_adicionar = tk.Button(frame, text='Adicionar Usuário', command=adicionar_usuario)
button_adicionar.grid(row=5, columnspan=2)

label_status = tk.Label(frame, text='', fg='green')
label_status.grid(row=6, columnspan=2)

root.mainloop()