from animal import Animal
from abc import ABC, abstractmethod

class Ave(Animal, ABC):
    @abstractmethod
    def __init__(self, tamanho_passo: int, altura_voo: int):
	    super().__init__(tamanho_passo)
        
    
    @property    
    @abstractmethod
    def altura_voo(self):
        return self.__altura_voo
    
    @altura_voo.setter
    @abstractmethod
    def altura_voo(self, altura: int):
        self.__altura_voo = altura
    
    @property
    @abstractmethod
    def tamanho_passo(self):
        return self.__tamanho_passo
    
    @tamanho_passo.setter
    @abstractmethod
    def tamanho_passo(self, tamanho: int):
        self.__tamanho_passo = tamanho
    
    @abstractmethod
    def mover(self):
        return "ANIMAL: DESLOCOU 3 VOANDO"
    
    @abstractmethod
    def produzir_som(self):
        return "AVE: PRODUZ SOM: PIU"