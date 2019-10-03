from entidades.pessoa import Pessoa
from entidades.endereco import Endereco
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
    
    @endereco.setter
    def endereco(self, cep: int, rua: str, numero: int, complemento: str):
        endereco = Endereco(cep, rua, numero, complemento)
        self.__endereco = endereco
        return "Endereco adicionado com sucesso!"
