from categoria_produto import CategoriaProduto
from cliente import Client

    def __init__(self, codigo, descricao, categoria="", quantida=0, preco_unitario=0, cliente=""):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__quantidade = quantidade
        self.__preco_unitario = preco_unitario
        self.__cliente = Cliente() #?? nao sei se da pra faze issu
    
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
    def categoria(self, categoria):
        self.__categoria = categoria
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
    
    @property
    def preco_unitario(self):
        return self.__preco_unitario
    
    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario
    
 
    
