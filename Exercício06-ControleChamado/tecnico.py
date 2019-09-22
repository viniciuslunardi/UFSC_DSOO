from pessoa import Pessoa


class Tecnico(Pessoa):
    def __init__(self, nome: str, codigo: int):
        self.__nome = nome
        self.__codigo = codigo
    
    @property
    def nome(self):
        return self.__nome 

    @property
    def codigo(self):
        return self.__codigo

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    @codigo.setter
    def codigo(self, cdg: int):
        self.__codigo = cdg
