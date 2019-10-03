from controladores.controladorPedido import ControladorPedido
from telas.telaPrincipal import TelaPrincipal
class ControladorRestaurante:
    def __init__(self):
        self.__controlador_pedido = ControladorPedido
        self.__tela_principal = TelaPrincipal(self)
    
    def escolher_login(self):
        self.__tela_principal.boas_vindas()
    
    