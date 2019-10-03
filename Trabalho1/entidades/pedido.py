from entidades.cliente import Cliente
class Pedido:
    def __init__(self, cliente: Cliente=None, feijao: bool=False, arroz: bool=False, macarrao: bool=False, 
        carne: bool=False, status: str="Pedido Criado."):
        self.__pedido = []
        self.__feijao = feijao
        self.__arroz = arroz
        self.__macarrao = macarrao
        self.__carne = carne
        self.__cliente = cliente
        self.__status = status
    
    @property
    def feijao(self, feijao: bool=True):
        self.__feijao = feijao
        self.__pedido.append(str("feijao"))
        return ("Feijao adicionado ao pedido.")
        
    @property
    def arroz(self, arroz: bool=True):
        self.__arroz = arroz
        self.__pedido.append(str("arroz"))
        return ("Arroz adicionado ao pedido.")

    @property
    def macarrao(self, macarrao: bool=True):
        self.__macarrao = macarrao
        self.__pedido.append(str("macarrao"))
        return ("Macarrao adicionado ao pedido.")

    @property
    def carne(self, carne: bool=True):
        self.__carne = carne
        self.__pedido.append(str("carne"))
        return "Carne adicionada ao pedido."
    
    @property
    def status(self):
        return self.__status
    
    @property
    def pedido(self):
        if self.__cliente not in self.__pedido: 
            self.__pedido.append(self.__cliente)
        if self.__status not in self.__pedido:
            self.__pedido.append(self.__status)
        return self.__pedido

    @status.setter
    def status(self, status: str):
        self.__pedido.remove(self.__status)
        self.__status = status
        self.__pedido.append(self.__status)


    def sair(self):
        exit(0)

        
