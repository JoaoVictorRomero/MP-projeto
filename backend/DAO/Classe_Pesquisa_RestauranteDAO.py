from .Conexao_BD import ConexaoBD
from .Classe_Pesquisa_Restaurante import Pesquisa_Restaurante
import mysql.connector

class Pesquisa_RestauranteDAO:
    '''Classe que define uma Pesquisa de Restaurantes do BD'''
    def adicionar_pesquisa_restaurante(self, pesquisa_restaurante: Pesquisa_Restaurante) -> bool:
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn
            cursor = conn.cursor()

            id_pesquisa_restaurante = pesquisa_restaurante.get_id_pesquisa_restaurante()
            fk_id_usuario = pesquisa_restaurante.get_fk_id_usuario()
            fk_id_restaurante = pesquisa_restaurante.get_fk_id_restaurante()
            
            sql = 'INSERT INTO pesquisas_restaurantes (id_pesquisa_restaurante, fk_id_usuario, fk_id_restaurante) VALUES (%s, %s, %s)'

            cursor.execute(sql, (id_pesquisa_restaurante, fk_id_usuario, fk_id_restaurante))
            conn.commit()
            
            return True

        except mysql.connector.Error as erro:
            print(f'Pesquisa_RestauranteDAO - Adicionar Pesquisa de Restaurante: {erro}')

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def buscar_pesquisas_restaurante_por_usuario(self, fk_id_usuario: int) -> Pesquisa_Restaurante:
        conexao = ConexaoBD()
        conexao.conecta_bd()

        lista_pesquisas = []

        try:
            conn = conexao.conn
            cursor = conn.cursor()

            sql = 'SELECT * FROM pesquisas_restaurantes WHERE fk_id_usuario = %s'
            
            cursor.execute(sql, (fk_id_usuario,))
            resultados = cursor.fetchall()

            for resultado in resultados:
                id_pesquisa_restaurante, fk_id_usuario, fk_id_restaurante = resultado

                pesquisa_restaurante = Pesquisa_Restaurante(id_pesquisa_restaurante, fk_id_usuario, fk_id_restaurante)
                lista_pesquisas.append(pesquisa_restaurante)

            return lista_pesquisas

        except mysql.connector.Error as erro:
            print(f'Pesquisa_RestauranteDAO - Buscar Pesquisas de Restaurante por Usuário: {erro}')

            return []

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def atualizar_pesquisa_restaurante(self, pesquisa_restaurante: Pesquisa_Restaurante) -> bool:
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn
            cursor = conn.cursor()

            id_pesquisa_restaurante = pesquisa_restaurante.get_id_pesquisa_restaurante()
            fk_id_usuario = pesquisa_restaurante.get_fk_id_usuario()
            fk_id_restaurante = pesquisa_restaurante.get_fk_id_restaurante()
            
            sql = 'UPDATE pesquisas_restaurantes SET fk_id_usuario = %s, fk_id_restaurante = %s WHERE id_pesquisa_restaurante = %s'

            cursor.execute(sql, (fk_id_usuario, fk_id_restaurante, id_pesquisa_restaurante))
            conn.commit()
            
            return True

        except mysql.connector.Error as erro:
            print(f'Pesquisa_RestauranteDAO - Atualizar Pesquisa de Restaurante: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def deletar_pesquisa_restaurante(self, id_pesquisa_restaurante: int) -> bool:
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn
            cursor = conn.cursor()

            sql = 'DELETE FROM pesquisas_restaurantes WHERE id_pesquisa_restaurante = %s'

            cursor.execute(sql, (id_pesquisa_restaurante,))
            conn.commit()
            
            return True

        except mysql.connector.Error as erro:
            print(f'Pesquisa_RestauranteDAO - Deletar Pesquisa de Restaurante: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()
