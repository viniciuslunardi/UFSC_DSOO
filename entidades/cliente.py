from entidades.pessoa import Pessoa
from entidades.endereco import Endereco
class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: int, telefone: str, 
        endereco: Endereco, fidelidade: int=0):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco
        self.__fidelidade = fidelidade
        self.__cliente = {'nome': self.nome, 'cpf': self.cpf, 'endereco': self.endereco,
        'telefone': self.telefone}
    
    @property
    def endereco(self):
        return self.__endereco.rua, self.__endereco.numero, self.__endereco.complemento
    
    @property
    def fidelidade(self):
        return self.__fidelidade
    
    @property
    def cliente(self):
        return self.__cliente
    
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
    
    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone
    