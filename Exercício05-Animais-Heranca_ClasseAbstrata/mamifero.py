from animal import Animal
from abc import ABC, abstractmethod

class Mamifero(Animal, ABC): 
    @abstractmethod
    def __init__(self, tamanho_passo: int, volume_som: int):
        super().__init__(tamanho_passo)
        self.__volume_som = volume_som
    
    @property    
    @abstractmethod
    def tamanho_passo(self):
        return self.__tamanho_passo
    
    @property
    @abstractmethod
    def volume_som(self):
        return self.__volume_som

    @tamanho_passo.setter
    @abstractmethod
    def tamanho_passo(self, tamanho: int):
        self.__tamanho_passo = tamanho

    @volume_som.setter
    @abstractmethod
    def volume_som(self, volume: int):
        self.__volume_som = volume    

    @abstractmethod
    def produzir_som(self):
        return "O mamifero produziu um som."