from entidades.pedido import Pedido
from telas.telaPedido import TelaPedido
class ControladorPedido:
    def __init__(self, controlador_principal):
        self.__pedidos = []
        self.__controlador_principal = controlador_principal
        self.__tela_pedido = TelaPedido(self)
    
    def cria_pedido(self):
        p1 = Pedido()
        while True:
            a = self.monta_prato(p1)
            if a:
                break
        return p1.pedido
        
    def monta_prato(self, pedido: Pedido):
        opcoes = {1: pedido.arroz, 2: pedido.feijao, 3: pedido.macarrao, 
        4: pedido.carne, 5: self.finaliza, 0: self.exit}
        opcao = self.__tela_pedido.mostra_tela_opcoes()
        funcao_escolhida = opcoes[opcao]    
        funcao_escolhida()
        if opcao == 5:
            return pedido.pedido     

    def finaliza(self):
        return False

    def ve_pedidos(self):
        if self.__pedidos:
            for i in self.__pedidos:
                print(i)
        else: 
            return "\nAtencao, nao existem pedidos abertos.\n" 

    def exit(self):
        exit(0)
    
