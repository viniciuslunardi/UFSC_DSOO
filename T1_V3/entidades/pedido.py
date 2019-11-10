class Pedido:
    def __init__(self):
        self.__pedido = []

    def feijao(self):
        self.__pedido.append("feijao")
    
    def arroz(self):
        self.__pedido.append("arroz")
    
    def macarrao(self):
        self.__pedido.append("macarrao")
    
    def carne(self):
        self.__pedido.append("carne")
        
    @property
    def pedido(self):
        return self.__pedido

    def sair(self):
        exit(0)
