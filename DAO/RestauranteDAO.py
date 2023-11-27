from conexao.ConexaoBD import ConexaoBD
from DTO.Restaurante import Restaurante
import mysql.connector

class RestauranteDAO():
    def adicionar_restaurante(self, restaurante):
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
