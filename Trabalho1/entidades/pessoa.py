from abc import ABC, abstractmethod
class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: str, telefone: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
    
    @property
    @abstractmethod
    def nome(self):
        return self.__nome
    
    @property
    @abstractmethod
    def cpf(self):
        return self.__cpf
    
    @property
    @abstractmethod
    def telefone(self):
        return self.__telefone
    
    @nome.setter
    @abstractmethod
    def nome(self, nome: str):
        self.__nome = nome
    
    @cpf.setter
    @abstractmethod
    def cpf(self, cpf: str):
        self.__cpf = cpf
    
    @telefone.setter
    @abstractmethod
    def telefone(self, telefone: str):
        self.__telefone = telefone

    @abstractmethod
    def __eq__(self, other):
        if self.cpf == other.cpf:
            return True
        else: return False