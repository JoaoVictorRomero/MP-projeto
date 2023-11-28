class Usuario():
    def __init__(self, id_usuario: int, nome_usuario: str, funcao: str, login: str, senha: str):
        self.id_usuario = id_usuario
        self.nome_usuario = nome_usuario
        self.funcao = funcao
        self.login = login
        self.senha = senha

    def setId_usuario(self, id_usuario: int):
        self.id_usuario = id_usuario

    def getId_usuario(self):
        return self.id_usuario
    
    def setNome_usuario(self, nome_usuario: str):
        self.nome_usuario = nome_usuario

    def getNome_usuario(self):
        return self.nome_usuario

    def setFuncao(self, funcao: str):
        self.funcao = funcao

    def getFuncao(self):
        return self.funcao

    def setLogin(self, login: str):
        self.login = login

    def getLogin(self):
        return self.login

    def setSenha(self, senha: str):
        self.senha = senha

    def getSenha(self):
        return self.senha
    

    def __str__(self):
        return f'ID Usuário: {self.id_usuario}\nNome: {self.nome_usuario}\nFunção: {self.funcao}\nLogin: {self.login}\n'