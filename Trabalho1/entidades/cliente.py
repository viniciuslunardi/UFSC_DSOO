from pessoa import Pessoa
from endereco import Endereco
class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, endereco: Endereco, 
        pedidos_anteriores: [], fidelidade: int=0):
        super().__init__(nome, cpf, telefone)
        self.__endereco = endereco
        self.__pedidos_anteriores = pedidos_anteriores
        self.__fidelidade = fidelidade
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def fidelidade(self):
        return self.__fidelidade
    
    @fidelidade.setter
    def fidelidade(self, fidelidade):
        self.__fidelidade = fidelidade
    
    @endereco.setter
    def endereco(self, endereco: Endereco):
        if (endereco is not None) and (isinstance(endereco, Endereco)):
            self.__endereco = endereco
    
          
       

