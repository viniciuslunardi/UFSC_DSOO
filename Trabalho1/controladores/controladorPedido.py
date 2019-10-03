from entidades.pedido import Pedido
from telas.telaPedido import TelaPedido
from entidades.cliente import Cliente
class ControladorPedido:
    def __init__(self):
        self.__pedidos = [{"cliente": Cliente.nome, "pedido": Pedido.pedido, "status": Pedido.status}]
        self.__clientes = []
        self.__tela_pedido = TelaPedido(self)
    
    def cadastrar_cliente(self, nome, cpf, telefone, endereco, fidelidade):
        c1 = Cliente(nome, cpf, telefone, endereco)
        self.__clientes.append(c1)
        return c1

    def criar_pedido(self):
        p1 = Pedido()
        while True:
            self.editar_pedido(p1)
    
    def editar_pedido(self, pedido: Pedido):
        produtos = {1: pedido.arroz, 2: pedido.feijao, 3: pedido.macarrao, 
        4: pedido.carne, 5: self.registrar_pedido, 0: self.__tela_pedido.sair}
        opcao = self.__tela_pedido.mostra_tela_opcoes()
        funcao_escolhida = produtos[opcao]
        if opcao == 0:
            funcao_escolhida()
        if opcao == 5:
            funcao_escolhida(pedido)
            self.entrou()
        else: print(funcao_escolhida)

    def entrou(self):
        switcher = {1: self.criar_pedido, 2: self.ver_pedidos,
        0: self.sair}
        while True: 
            opcao = self.__tela_pedido.mostra_tela_cliente()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def registrar_pedido(self, p1: Pedido):
        self.__pedidos.append(p1.pedido)
        p1.status = "Pedido realizado."
        print("Pedido realizado.")
    
    def ver_pedidos(self):
        return self.__pedidos

    def sair(self):
        exit(0)