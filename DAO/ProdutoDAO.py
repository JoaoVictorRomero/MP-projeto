from conexao.ConexaoBD import ConexaoBD
from DTO.Produto import Produto
import mysql.connector

class ProdutoDAO():
    def adicionar_produto(self, produto: Produto) -> bool:
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            id_produto = produto.get_id_produto()
            nome_produto = produto.get_nome_produto()
            fk_id_restaurante = produto.get_fk_id_restaurante()
            
            sql = 'INSERT INTO produtos (id_produto, nome_produto, fk_id_restaurante) VALUES (%s, %s, %s)'

            cursor.execute(sql, (id_produto, nome_produto, fk_id_restaurante))
            conn.commit()
            print('Produto adicionado com sucesso!')

            return True

        except mysql.connector.Error as erro:
            print(f'ProdutoDAO - Adicionar Produto: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def pesquisar_produtos(self) -> list:
            conexao = ConexaoBD()
            conexao.conecta_bd()

            listaProdutos = list()

            try:
                conn = conexao.conn #Obtém a conexão com o BD
                cursor = conn.cursor()

                sql = 'SELECT * FROM produtos'

                cursor.execute(sql)
                resultado = cursor.fetchall()

                for linha in resultado:
                    id_produto, nome_produto, fk_id_restaurante = linha
                    
                    produto = Produto(id_produto, nome_produto, fk_id_restaurante)

                    listaProdutos.append(produto)

                print('Produtos listados com sucesso!')
                
                return listaProdutos

            except mysql.connector.Error as erro:
                print(f'ProdutoDAO - Pesquisar Produtos: {erro}')
                return []

            finally:
                cursor.close()
                conexao.desconecta_bd()

    def atualizar_produto(self, produto: Produto) -> bool:
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            id_produto = produto.get_id_produto()
            nome_produto = produto.get_nome_produto()
            fk_id_restaurante = produto.get_fk_id_restaurante()
            
            sql = 'UPDATE produtos SET nome_produto = %s, fk_id_restaurante = %s WHERE id_produto = %s'

            cursor.execute(sql, (nome_produto, fk_id_restaurante, id_produto))
            conn.commit()
            print('Produto atualizado com sucesso!')

            return True

        except mysql.connector.Error as erro:
            print(f'ProdutoDAO - Atualizar Produto: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def deletar_produto(self, id_produto: int) -> bool:
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            sql = 'DELETE FROM produtos WHERE id_produto = %s'

            cursor.execute(sql, (id_produto,))
            conn.commit()
            print('Produto excluído com sucesso!')

            return True

        except mysql.connector.Error as erro:
            print(f'ProdutoDAO - Deletar Produto: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()
