from entidades.pedido import Pedido
from telas.telaPedido import TelaPedido
class ControladorPedido:
    def __init__(self):
        self.__pedidos = []
        self.__tela_pedido = TelaPedido(self)
    
    def criar_pedido(self):
        p1 = Pedido()
        while True:
            self.editar_pedido(p1)
    
    def editar_pedido(self, pedido: Pedido):
        produtos = [{1: pedido.arroz},
        {2: pedido.feijao}, {3: pedido.macarrao}, {4: pedido.carne}, {0: pedido.exit}]
        opcao = self.__tela_pedido.mostra_tela_opcoes()
        funcao_escolhida = produtos[opcao]
        funcao_escolhida
        if opcao == int(0):
            funcao_escolhida(opcao)
