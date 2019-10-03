from entidades.pedido import Pedido
from telas.telaPedido import TelaPedido
from telas.telaFuncionario import TelaFuncionario
from entidades.cliente import Cliente
from telas.telaCliente import TelaCliente
import random
class ControladorPedido:
    def __init__(self):
        self.__pedidos = []
        self.__clientes = []
        self.__pedido = {"cliente": Cliente.nome, "pedido": Pedido.pedido, 
        "status": "", "codigo": random.randrange(1,399)}
        self.__cliente = {"nome": Cliente.nome, "endereco": Cliente.endereco, 
        "telefone": Cliente.telefone}
        self.__tela_pedido = TelaPedido(self)
        self.__tela_funcionario = TelaFuncionario(self)
        self.__tela_cliente = TelaCliente(self)
    
    def cadastrar_cliente(self, nome: str="", cpf: str="", telefone: str="", rua: str="", numero: int=0, 
    complemento: str="", cep: int=88040320):
        novo_end = Cliente.endereco = rua, numero, complemento, cep
        c1 = Cliente(nome, cpf, telefone, novo_end)
        self.__pedido['cliente'] = c1
        return c1

    def criar_pedido(self):
        p1 = Pedido()
        while True:
            self.editar_pedido(p1)
    
    def editar_pedido(self, pedido: Pedido):
        produtos = {1: pedido.arroz, 2: pedido.feijao, 3: pedido.macarrao, 
        4: pedido.carne, 5: self.registra_pedido_novo, 6: self.registra_pedido_cadastrado, 0: self.__tela_pedido.sair}
        opcao = self.__tela_pedido.mostra_tela_opcoes()
        funcao_escolhida = produtos[opcao]
        if opcao == 0:
            funcao_escolhida()
        if opcao == 5:
            funcao_escolhida(pedido)
            self.entrou_cliente()
        if opcao == 6:
            funcao_escolhida(pedido)
            self.entrou_cliente()
        else: 
            funcao_escolhida
            print(funcao_escolhida)

    def entrou_cliente(self):
        switcher = {1: self.criar_pedido, 2: self.ver_pedidos, 3: self.mostra_tela_cadastro,
        0: self.sair}
        while True: 
            opcao = self.__tela_cliente.mostra_tela_cliente()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
    
    def entrou_funcionario(self):
        switcher = {1: self.ver_pedidos, 0: self.sair}
        while True: 
            opcao = self.__tela_funcionario.mostra_tela_funcionario()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def registra_pedido_novo(self, p1: Pedido):
        nome = self.__tela_cliente.cadastro()
        self.__pedido['cliente'] = nome
        self.__pedido['pedido'] = p1.pedido
        self.__pedido['status'] = "Pedido realizado"
        self.__pedido['codigo'] = random.randrange(1,900)
        self.__pedidos.append(self.__pedido)

    def registra_pedido_cadastrado(self, p1: Pedido):
        self.__pedido['cliente'] = Cliente.nome
        self.__pedido['pedido'] = p1.pedido
        self.__pedido['status'] = "Pedido realizado"
        self.__pedido['codigo'] = random.randrange(1,900)
        self.__pedidos.append(self.__pedido)
    
    def ver_pedidos(self):
        print(('\n{}').format(self.__pedidos))
        return False

    def mostra_tela_cadastro(self):
        nome = self.__tela_cliente.cadastro()
        return nome

    def sair(self):
        exit(0)