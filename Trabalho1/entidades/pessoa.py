class Pessoa:
    def __init__(self, nome: str, cpf: str, telefone: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
    
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
    def cpf(self, cpf: str):
        self.__cpf = cpf
    
    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone