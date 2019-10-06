from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, capacidade: int, totalPessoas: int, totalAndaresPredio: int, andarAtual: int):
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas
        self.__andarAtual = andarAtual
        self.__totalAndaresPredio = totalAndaresPredio
    
    # ElevadorJahNoTerreoException
    def descer(self) -> str:
    	if self.__andarAtual == int(1):
            return ElevadorJahNoTerreoException()
    
    # ElevadorCheioException
    def entraPessoa(self) -> str:
    	if self.__totalPessoas == self.__capacidade:
            return ElevadorCheioException()
    
    # ElevadorJahVazioException
    def saiPessoa(self) -> str:
    	if self.__totalPessoas == int(0):
            return ElevadorJahVazioException()
    
    # ElevadorJahNoUltimoAndarException
    def subir(self) -> str:
    	if self.__andarAtual == self.__totalAndaresPredio:
            return ElevadorJahNoUltimoAndarException()
    
    @property
    def capacidade(self) -> int:
    	return self.__capacidade
    
    @property
    def totalPessoas(self) -> int:
    	return self.__totalPessoas
    
    @property
    def totalAndaresPredio(self) -> int:
    	return self.__totalAndaresPredio
    
    @property
    def andarAtual(self) -> int:
    	return self.__andarAtual
    
    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int):
    	self.__totalAndaresPredio = totalAndaresPredio



    