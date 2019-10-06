from controladores.controladorPedido import ControladorPedido
from telas.telaPrincipal import TelaPrincipal
from telas.telaFuncionario import TelaFuncionario
class ControladorRestaurante:
    def __init__(self):
        self.__controlador_pedido = ControladorPedido()
        self.__tela_principal = TelaPrincipal(self)
        self.__tela_funcionario = TelaFuncionario(self)
    
    def inicia(self):
        switcher = {2: self.abre_tela_cliente,
        1: self.abre_tela_funcionario, 0: self.sair}
        while True:
            opcao = self.__tela_principal.boas_vindas()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
    
    def abre_tela_cliente(self):
        self.__controlador_pedido.entrou_cliente()

    def abre_tela_funcionario(self):
        self.__controlador_pedido.entrou_funcionario()
    
    def sair(self):
        exit(0)