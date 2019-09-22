class Endereco:
    def __init__(self, cep: int, rua: str, numero: int, complemento: str):
        self.__cep = cep
        self.__rua = rua
        self.__numero = numero
        self.__complemento = complemento

    @property
    def cep(self):
        return self.__cep
    
    @cep.setter
    def cep(self, cep: int):
        self.__cep = cep

    @property
    def rua(self):
        return self.__rua
    
    @rua.setter
    def rua(self, rua: str):
        self.__rua = rua
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero: int):
        self.__numero = numero

    @property
    def complemento(self):
        return self.__complemento
    
    @complemento.setter
    def complemento(self, cp: str):
        self.__complemento = cp