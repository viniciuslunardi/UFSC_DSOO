from categoria_produto import CategoriaProduto as cp
from cliente import Cliente
class Produto:

    def __init__(self,codigo,descricao,categoria_produto="",qtd=0,preco_unitario=0,Cliente=""):
        self.__codigo = codigo
        self.__descricao = descricao 
        self.__categoria_produto = categoria_produto
        self.__preco_unitario = preco_unitario
        self.__Cliente = Cliente
    
    @property
    def codigo(self):
        return self.__codigo
        
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo = codigo