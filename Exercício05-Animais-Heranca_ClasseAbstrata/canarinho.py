from ave import Ave

class Canarinho(Ave):
    def __init__(self, tamanho_passo: int, volume_som: int):
        super().__init__(tamanho_passo, volume_som)

    @property
    def altura_voo(self):
        return self.__altura_voo
    
    @altura_voo.setter
    def altura_voo(self, altura: int):
        self.__altura_voo = altura
    
    @property
    def tamanho_passo(self):
        return self.__tamanho_passo
        
    @tamanho_passo.setter
    def tamanho_passo(self, tamanho: int):
        self.__tamanho_passo = tamanho
    
    def mover(self):
        return "ANIMAL: DESLOCOU 3 VOANDO"
    
    def produzir_som(self):
        return self.__volume_som

    def cantar(self):
        return "AVE: PRODUZ SOM: PIU"