from conexao.ConexaoBD import ConexaoBD
from DTO.Restaurante import Restaurante
import mysql.connector

class RestauranteDAO():
    '''Classe que define um Restaurante do BD'''
    def adicionar_restaurante(self, restaurante):
        '''Função que adiciona um restaurante ao BD'''
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            id_restaurante = restaurante.get_id_restaurante()
            nome_restaurante = restaurante.get_nome_restaurante()
            distancia_totem = restaurante.get_distancia_totem()
            
            sql = 'INSERT INTO restaurantes (id_restaurante, nome_restaurante, distancia_totem) VALUES (%s, %s, %s)'

            cursor.execute(sql, (id_restaurante, nome_restaurante, distancia_totem))
            conn.commit()
            print('Restaurante adicionado com sucesso!')

            return True

        except mysql.connector.Error as erro:
            print(f'RestauranteDAO - Adicionar Restaurante: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def pesquisar_restaurantes(self) -> list:
            '''Função que retorna todos os restaurantes do BD'''
            conexao = ConexaoBD()
            conexao.conecta_bd()

            listaRestaurantes = list()

            try:
                conn = conexao.conn #Obtém a conexão com o BD
                cursor = conn.cursor()

                sql = 'SELECT * FROM restaurantes'

                cursor.execute(sql)
                resultado = cursor.fetchall()

                for linha in resultado:
                    id_restaurante, nome_restaurante, fk_id_restaurante = linha
                    
                    restaurante = Restaurante(id_restaurante, nome_restaurante, fk_id_restaurante)

                    listaRestaurantes.append(restaurante)

                print('Restaurantes listados com sucesso!')
                
                return listaRestaurantes

            except mysql.connector.Error as erro:
                print(f'RestauranteDAO - Pesquisar Restaurantes: {erro}')
                return []

            finally:
                cursor.close()
                conexao.desconecta_bd()

    def atualizar_restaurante(self, restaurante: Restaurante) -> bool:
        '''Função que atualiza um restaurante do BD com base no seu id'''
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            id_restaurante = restaurante.get_id_restaurante()
            nome_restaurante = restaurante.get_nome_restaurante()
            distancia_totem = restaurante.get_distancia_totem()
            
            sql = 'UPDATE restaurantes SET nome_restaurante = %s, distancia_totem = %s WHERE id_restaurante = %s'

            cursor.execute(sql, (nome_restaurante, distancia_totem, id_restaurante))
            conn.commit()
            print('Restaurante atualizado com sucesso!')

            return True

        except mysql.connector.Error as erro:
            print(f'RestauranteDAO - Atualizar Restaurante: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()

    def deletar_restaurante(self, id_restaurante: int) -> bool:
        '''Função que remove um restaurante do BD com base no seu id'''
        conexao = ConexaoBD()
        conexao.conecta_bd()

        try:
            conn = conexao.conn #Obtém a conexão com o BD
            cursor = conn.cursor()

            sql = 'DELETE FROM restaurantes WHERE id_restaurante = %s'

            cursor.execute(sql, (id_restaurante,))
            conn.commit()
            print('Restaurante excluído com sucesso!')

            return True

        except mysql.connector.Error as erro:
            print(f'RestauranteDAO - Deletar Restaurante: {erro}')

            return False

        finally:
            cursor.close()
            conexao.desconecta_bd()
