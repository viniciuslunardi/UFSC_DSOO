from entidades.pessoa import Pessoa
from entidades.endereco import Endereco
class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, 
        endereco: Endereco, fidelidade: int=0):
        super().__init__(nome, cpf, telefone)
        self.__endereco = endereco
        self.__fidelidade = fidelidade
    
    @property
    def endereco(self):
        return self.__endereco.rua, self.__endereco.numero, self.__endereco.complemento
    
    @property
    def fidelidade(self):
        return self.__fidelidade
    
    @endereco.setter
    def endereco(self, cep: int, rua: str, numero: int, complemento: str):
        endereco = Endereco(cep, rua, numero, complemento)
        self.__endereco = endereco
        return "Endereco adicionado com sucesso!"
