class Pedido:
    def __init__(self):
        self.__pedido = []
        self.__feijao = "feijao"
        self.__arroz = "arroz"
        self.__macarrao = "macarrao"
        self.__carne = "carne"
    
    @property
    def feijao(self):
        self.__pedido.append(self.__feijao)
        return ("Feijao adicionado ao pedido.")
        
    @property
    def arroz(self):
        self.__pedido.append(str("arroz"))
        return ("Arroz adicionado ao pedido.")

    @property
    def macarrao(self):
        self.__pedido.append(str("macarrao"))
        return ("Macarrao adicionado ao pedido.")

    @property
    def carne(self):
        self.__pedido.append(str("carne"))
        return "Carne adicionada ao pedido."
    
    @property
    def pedido(self):
        return self.__pedido

    def sair(self):
        exit(0)
