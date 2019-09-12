from pessoa import Pessoa
class Administrador(Pessoa):
    def __init__(self, nome: str, cpf: str, vendor: int):
        super().__init__(nome, cpf)
        self.__vendor = vendor
    
    @property
    def vendor(self):
        return self.__vendor
    
    @vendor.setter
    def vendor(self, vendor: int):
        self.__vendor = vendor
    
    