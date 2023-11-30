from .Conexao_BD import ConexaoBD
from .Classe_Pesquisa_Produto import Pesquisa_Produto
import mysql.connector

class Pesquisa_ProdutoDAO:
    '''Classe que define uma Pesquisa de Produtos do BD'''
    def adicionar_pesquisa_produto(self, pesquisa_produto: Pesquisa_Produto) -> bool:
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn
            cursor = conn.cursor()

            id_pesquisa_produto = pesquisa_produto.get_id_pesquisa_produto()
            fk_id_usuario = pesquisa_produto.get_fk_id_usuario()
            fk_id_produto = pesquisa_produto.get_fk_id_produto()
            
            sql = 'INSERT INTO pesquisas_produtos (id_pesquisa_produto, fk_id_usuario, fk_id_produto) VALUES (%s, %s, %s)'

            cursor.execute(sql, (id_pesquisa_produto, fk_id_usuario, fk_id_produto))
            conn.commit()
            
            return True

        except mysql.connector.Error as erro:
            print(f'Pesquisa_ProdutoDAO - Adicionar Pesquisa de Produto: {erro}')

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def buscar_pesquisas_produto_por_usuario(self, fk_id_usuario: int) -> Pesquisa_Produto:
        conexao = ConexaoBD()
        conexao.conecta_bd()

        lista_pesquisas = []

        try:
            conn = conexao.conn
            cursor = conn.cursor()

            sql = 'SELECT * FROM pesquisas_produtos WHERE fk_id_usuario = %s'
            
            cursor.execute(sql, (fk_id_usuario,))
            resultados = cursor.fetchall()

            for resultado in resultados:
                id_pesquisa_produto, fk_id_usuario, fk_id_produto = resultado

                pesquisa_produto = Pesquisa_Produto(id_pesquisa_produto, fk_id_usuario, fk_id_produto)
                lista_pesquisas.append(pesquisa_produto)

            return lista_pesquisas

        except mysql.connector.Error as erro:
            print(f'Pesquisa_ProdutoDAO - Buscar Pesquisas de Produto por Usuário: {erro}')

            return []

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def atualizar_pesquisa_produto(self, pesquisa_produto: Pesquisa_Produto) -> bool:
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn
            cursor = conn.cursor()

            id_pesquisa_produto = pesquisa_produto.get_id_pesquisa_produto()
            fk_id_usuario = pesquisa_produto.get_fk_id_usuario()
            fk_id_produto = pesquisa_produto.get_fk_id_produto()
            
            sql = 'UPDATE pesquisas_produtos SET fk_id_usuario = %s, fk_id_produto = %s WHERE id_pesquisa_produto = %s'

            cursor.execute(sql, (fk_id_usuario, fk_id_produto, id_pesquisa_produto))
            conn.commit()
            
            return True

        except mysql.connector.Error as erro:
            print(f'Pesquisa_ProdutoDAO - Atualizar Pesquisa de Produto: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def deletar_pesquisa_produto(self, id_pesquisa_produto: int) -> bool:
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn
            cursor = conn.cursor()

            sql = 'DELETE FROM pesquisas_produtos WHERE id_pesquisa_produto = %s'

            cursor.execute(sql, (id_pesquisa_produto,))
            conn.commit()
            
            return True

        except mysql.connector.Error as erro:
            print(f'Pesquisa_ProdutoDAO - Deletar Pesquisa de Produto: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()
