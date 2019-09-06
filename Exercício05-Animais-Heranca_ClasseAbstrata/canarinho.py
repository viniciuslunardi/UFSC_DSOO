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
    
    def mover(self):
        return "O passaro voou {self.__altura_voo} metros."

    def cantar(self):
        return "AVE: PRODUZ SOM: PIU"