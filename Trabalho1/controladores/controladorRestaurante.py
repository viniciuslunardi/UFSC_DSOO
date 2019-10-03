from controladores.controladorPedido import ControladorPedido
from telas.telaPrincipal import TelaPrincipal
class ControladorRestaurante:
    def __init__(self):
        self.__controlador_pedido = ControladorPedido()
        self.__tela_principal = TelaPrincipal(self)
    
    def inicia(self):
        switcher = {2: self.abre_tela_cliente,
        1: self.abre_tela_funcionario}
        while True:
            opcao = self.__tela_principal.boas_vindas()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
    
    def abre_tela_cliente(self):
        self.__controlador_pedido.entrou()

    def abre_tela_funcionario(self):
        pass