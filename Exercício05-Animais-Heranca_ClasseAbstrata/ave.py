from animal import Animal

class Ave(Animal):
    def __init__(self, tamanho_passo: int, altura_voo: int):
	    super().__init__(tamanho_passo)
        self.__altura_voo = altura_voo    

    @property
    def altura_voo(self):
        return self.__altura_voo
    
    @altura_voo.setter
    def altura_voo(self, altura: int):
        self.__altura_voo = altura
    
    def mover(self):
        return "O passaro voou {self.__altura_voo} metros."

    def produzir_som(self):
        return "AVE: PRODUZ SOM: PIU"