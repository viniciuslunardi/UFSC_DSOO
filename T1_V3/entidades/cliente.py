from entidades.pessoa import Pessoa
from entidades.endereco import Endereco
class Cliente(Pessoa):
    def __init__(self, cpf: int, nome: str, telefone: str, 
        endereco: Endereco, fidelidade: int=0, senha: int=1234):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco
        self.__rua = endereco.rua
        self.__numero = endereco.numero
        self.__complemento = endereco.complemento
        self.__fidelidade = fidelidade
        self.__senha = senha
    
    @property
    def rua(self):
        return self.__rua
    
    @property
    def numero(self):
        return self.__numero

    @property
    def complemento(self):
        return self.__complemento

    @property
    def endereco(self):
        return self.__endereco.rua, self.__endereco.numero, self.__endereco.complemento
    
    @property
    def fidelidade(self):
        return self.__fidelidade
    
    @property
    def senha(self):
        return self.__senha
    
    @endereco.setter
    def endereco(self, cep: int, rua: str, numero: int, complemento: str):
        endereco = Endereco(cep, rua, numero, complemento)
        self.__endereco = endereco
        return "Endereco adicionado com sucesso!"

    def __eq__(self, other):
        if self.cpf == other.cpf:
            return True
        else: return False
    
    def __str__(self):
        return "Nome: {}, cpf: {}, telefone: {}, endereco: {}".format(self.nome, self.cpf, self.telefone, self.endereco)

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def telefone(self):
        return self.__telefone
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf
    
    @senha.setter
    def senha(self, senha: int):
        self.__senha = senha

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone
    
