from animal import Animal

class Mamifero(Animal): 
    def __init__(self, tamanho_passo: int, volume_som: int):
        super().__init__(tamanho_passo)
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
    
    def produzir_som(self):
        return "O mamifero produziu um som."