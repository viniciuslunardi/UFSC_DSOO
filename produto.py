from cliente import Cliente
from categoria_produto import CategoriaProduto


class Produto:
    def __init__(self, codigo, descricao, categoria,
                 cliente='', preco_unitario=0.0, qtd=0):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria = categoria
        self.__cliente = cliente
        self.__preco_unitario = preco_unitario
        self.__quantidade = qtd

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, titulo):
        self.__categoria = CategoriaProduto(titulo)

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, qtd):
        self.__quantidade = qtd

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, nome: str):
        self.__cliente = nome

    def preco_total(self):
        return (self.__quantidade * self.__preco_unitario)
