from mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self, tamanho_passo: int=2, volume_som: int=2):
        super().__init__(tamanho_passo, volume_som)
        self.__volume_som = volume_som

    @property
    def tamanho_passo(self):
        return self.__tamanho_passo
    
    @property
    def volume_som(self):
        return self.__volume_som
    
    @tamanho_passo.setter
    def tamanho_passo(self, tamanho: int):
        self.__tamanho_passo = tamanho
    
    @volume_som.setter
    def volume_som(self, volume: int):
        self.__volume_som = volume
    
    def mover(self):
        return "ANIMAL: DESLOCOU 2"
    
    def produzir_som(self):
        return self.__volume_som
    
    def miar(self):
        return "MAMIFERO: PRODUZ SOM: "+ str(self.__volume_som)+ " SOM: MIAU"
    