from entidades.pedido import Pedido
from telas.telaPedido import TelaPedido
from telas.telaFuncionario import TelaFuncionario
from entidades.cliente import Cliente
import random
class ControladorPedido:

    def __init__(self):
        self.__pedidos = [{"cliente": Cliente.nome, "pedido": Pedido.pedido, 
        "status": Pedido.status, "codigo": random.randrange(1,399)}]
        self.__clientes = [{"nome": Cliente.nome, "endereco": Cliente.endereco, 
        "telefone": Cliente.telefone}]
        self.__tela_pedido = TelaPedido(self)
        self.__tela_funcionario = TelaFuncionario(self)
    
    def cadastrar_cliente(self, nome, cpf, telefone, ):
        novo_end = Cliente.endereco = 'nome'
        c1 = Cliente(nome, cpf, telefone, novo_end)
        
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
            self.entrou_cliente()
        else: print(funcao_escolhida)

    def entrou_cliente(self):
        switcher = {1: self.criar_pedido, 2: self.ver_pedidos,
        0: self.sair}
        while True: 
            opcao = self.__tela_pedido.mostra_tela_cliente()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
    
    def entrou_funcionario(self):
        switcher = {1: self.ver_pedidos, 0: self.sair}
        while True: 
            opcao = self.__tela_funcionario.mostra_tela_funcionario()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def registrar_pedido(self, p1: Pedido):
        self.__pedidos.append(p1.pedido)
        p1.status = "Pedido realizado."
        print("Pedido realizado.")
    
    def ver_pedidos(self):
        print(('\n oiiiiiiiiii, seu pedido eh este {}').format(self.__pedidos))
        return False

    def sair(self):
        exit(0)