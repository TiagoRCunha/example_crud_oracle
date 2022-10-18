from datetime import date
from model.card import Card
from model.album import Album

class User:
    def __init__(self, 
                 codigo_pedido:int=None,
                 data_pedido:date=None,
                 cliente:Card= None,
                 fornecedor:Album=None
                 ):
        self.set_codigo_pedido(codigo_pedido)
        self.set_data_pedido(data_pedido)
        self.set_cliente(cliente)
        self.set_fornecedor(fornecedor)


    def set_codigo_pedido(self, codigo_pedido:int):
        self.codigo_pedido = codigo_pedido

    def set_data_pedido(self, data_pedido:date):
        self.data_pedido = data_pedido

    def set_cliente(self, cliente:Card):
        self.cliente = cliente

    def set_fornecedor(self, fornecedor:Album):
        self.fornecedor = fornecedor

    def get_codigo_pedido(self) -> int:
        return self.codigo_pedido

    def get_data_pedido(self) -> date:
        return self.data_pedido

    def get_cliente(self) -> Card:
        return self.cliente

    def get_fornecedor(self) -> Album:
        return self.fornecedor

    def to_string(self) -> str:
        return f"Pedido: {self.get_codigo_pedido()} | Data: {self.get_data_pedido()} | Cliente: {self.get_cliente().get_name()} | Fornecedor: {self.get_fornecedor().get_nome_fantasia()}"