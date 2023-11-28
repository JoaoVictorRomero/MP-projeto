class Restaurante():
    def __init__(self, id_restaurante: int, nome_restaurante: str, distancia_totem: float):
        self.id_restaurante = id_restaurante
        self.nome_restaurante = nome_restaurante
        self.distancia_totem = distancia_totem

    def get_id_restaurante(self):
        return self.id_restaurante

    def set_id_restaurante(self, id_restaurante: int):
        self.id_restaurante = id_restaurante

    def get_nome_restaurante(self):
        return self.nome_restaurante

    def set_nome_restaurante(self, nome_restaurante: str):
        self.nome_restaurante = nome_restaurante

    def get_distancia_totem(self):
        return self.distancia_totem

    def set_distancia_totem(self, distancia_totem: float):
        self.distancia_totem = distancia_totem


    def __str__(self):
        return f'ID do Restaurante: {self.id_restaurante}\nNome do Restaurante: {self.nome_restaurante}'