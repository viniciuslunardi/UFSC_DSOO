class Pedido:
    def __init__(self):
        self.__pedido = []

    def feijao(self):
        self.__pedido.append("feijao")
        return print("feijao adicionado com sucesso.")
    
    def arroz(self):
        self.__pedido.append("arroz")
        return print("Arroz adicionado com sucesso.")
    
    def macarrao(self):
        self.__pedido.append("macarrao")
        return print("Macarrao adicionado com sucesso.")
    
    def carne(self):
        self.__pedido.append("carne")
        return print("Carne adicionado com sucesso.")
        
    @property
    def pedido(self):
        return self.__pedido

    def sair(self):
        exit(0)
