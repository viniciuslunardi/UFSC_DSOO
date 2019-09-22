from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa


class Pessoa(AbstractPessoa, ABC):
    @abstractmethod
    def __init__(self, nome: str, codigo: int):
        self.__nome = nome
        self.__codigo = codigo

    @property
    @abstractmethod
    def nome(self):
        return self.__nome
    
    @property
    @abstractmethod
    def codigo(self):
        return self.__codigo
    
    @nome.setter
    @abstractmethod
    def nome(self, nome: str):
        self.__nome = nome
    
    @codigo.setter
    @abstractmethod
    def codigo(self, cdg: int):
        self.__codigo = cdg
