class Capitulo:
    def __init__(self, numero: int, titulo: str):
        self.__numero = numero
        self.__titulo = titulo

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self,nmr):
        self.__numero = nmr

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self,titulo):
        self.__titulo = titulo
