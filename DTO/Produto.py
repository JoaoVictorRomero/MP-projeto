class Produto():
    def __init__(self, id_produto: int, nome_produto: str, fk_id_restaurante: int):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.fk_id_restaurante = fk_id_restaurante

    def get_id_produto(self):
        return self.id_produto

    def set_id_produto(self, id_produto: int):
        self.id_produto = id_produto

    def get_nome_produto(self):
        return self.nome_produto

    def set_nome_produto(self, nome_produto: str):
        self.nome_produto = nome_produto

    def get_fk_id_restaurante(self):
        return self.fk_id_restaurante

    def set_fk_id_restaurante(self, fk_id_restaurante: int):
        self.fk_id_restaurante = fk_id_restaurante

    
    def __str__(self):
        return f'ID do Produto: {self.id_produto}, Nome do Produto: {self.nome_produto}, ID do Restaurante {self.fk_id_restaurante}'
        