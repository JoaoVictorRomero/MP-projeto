import sys
sys.path.append('./conexao')
sys.path.append('./DTO')

from ConexaoBD import ConexaoBD
from Usuario import Usuario

import mysql.connector

conn = ConexaoBD().conectaBD()

class UsuarioDAO():
    def __init__(self):
        self.conn = conn

    def adicionarUsuario(self, usuario):
        id_usuario = usuario.getId_usuario()
        nome_usuario = usuario.getNome_usuario()
        funcao = usuario.getFuncao()
        login = usuario.getLogin()
        senha = usuario.getSenha()
        
        sql = 'INSERT INTO usuarios (id_usuario, nome_usuario, funcao, login, senha) VALUES (%s, %s, %s, %s, %s)'

        try:
            ConexaoBD().executaDML(sql)
            print('Entrou')

        except mysql.connector.Error as error:
            print(f'UsuarioDAO Adicionar Usuário: {erro}')
    


print(ConexaoBD().executaDQL('SELECT * FROM usuarios'))