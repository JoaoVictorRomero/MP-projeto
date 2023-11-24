class Usuario:
    def __init__(self, id_usuario: int, nome_usuario: str, funcao: str, login: str, senha: str):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.funcao = funcao
        self.login = login
        self.senha = senha

    def get_id_usuario(self):
        return self.id_usuario

    def get_nome_usuario(self):
        return self.nome_usuario

    def get_funcao(self):
        return self.funcao

    def get_login(self):
        return self.login

    def get_senha(self):
        return self.senha

    def set_id_usuario(self, id_usuario: int):
        self.id_usuario = id_usuario

    def set_nome_usuario(self, nome_usuario: str):
        self.nome_usuario = nome_usuario

    def set_funcao(self, funcao: str):
        self.funcao = funcao

    def set_login(self, login: str):
        self.login = login

    def set_senha(self, senha: str):
        self.senha = senha

    def __str__(self):
        return f'ID Usuário: {self.id_usuario}, Nome: {self.nome_usuario}, Função: {self.funcao}, Login: {self.login}'

    

usuario = Usuario(1, 'Marcelo Vitor', 'Admin', 'marcelovitor@gmail.com', '123')

print(usuario)