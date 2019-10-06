from entidades.pedido import Pedido
from telas.telaPedido import TelaPedido
from telas.telaFuncionario import TelaFuncionario
from entidades.cliente import Cliente
from telas.telaCliente import TelaCliente
from telas.telaPrincipal import TelaPrincipal
import random
class ControladorPedido:
    def __init__(self):
        self.__pedidos = []
        self.__clientes = []
        self.__pedido = {"cliente": Cliente.nome, 
        "pedido": Pedido.pedido, "status": "", "codigo": random.randrange(1,399)}
        self.__cliente = {"nome": Cliente.nome, "cpf": Cliente.cpf, 
        "endereco": Cliente.endereco, "telefone": Cliente.telefone}
        self.__tela_pedido = TelaPedido(self)
        self.__tela_funcionario = TelaFuncionario(self)
        self.__tela_cliente = TelaCliente(self)
        self.__tela_principal = TelaPrincipal(self)
    
    def cadastrar_cliente(self):
        novo_cliente = self.__tela_funcionario.mostra_tela_cadastro_cliente()
        self.__cliente['nome'] = novo_cliente.nome
        self.__cliente['cpf'] = novo_cliente.cpf
        self.__cliente['endereco'] = novo_cliente.endereco
        self.__cliente['telefone'] = novo_cliente.telefone
        if self.__cliente['cpf'] not in self.__clientes:
            self.__clientes.append(self.__cliente)
            print(("Cliente {} cadastrado com sucesso.").format(self.__cliente['nome']))
        else: print("Impossivel cadastrar clientes com o mesmo cpf!")
    
    def criar_pedido(self):
        p1 = Pedido()
        while True:
            self.editar_pedido(p1)
    
    def editar_pedido(self, pedido: Pedido):
        produtos = {1: pedido.arroz, 2: pedido.feijao, 3: pedido.macarrao, 
        4: pedido.carne, 5: self.registra_pedido_novo, 6: self.registra_pedido_cadastrado, 0: self.__tela_pedido.sair}
        opcao = self.__tela_pedido.mostra_tela_opcoes()
        funcao_escolhida = produtos[opcao]
        if opcao == 5:
            funcao_escolhida(pedido)
            self.entrou_cliente()
        elif opcao == 6:
            funcao_escolhida(pedido, "Rafael")
            self.entrou_cliente()
        else:
            funcao_escolhida()

    def entrou_cliente(self):
        switcher = {1: self.criar_pedido, 2: self.ver_pedidos,
        9: self.voltar_tela_inicial, 0: self.sair}
        while True: 
            opcao = self.__tela_cliente.mostra_tela_cliente()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
    
    def entrou_funcionario(self):
        switcher = {0: self.sair, 1: self.ver_pedidos, 2: self.cadastrar_cliente, 3: self.ver_clientes}
        while True: 
            opcao = self.__tela_funcionario.mostra_tela_funcionario()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def registra_pedido_novo(self, p1: Pedido):
        novo_cliente = self.__tela_cliente.cadastro()
        self.__pedido['pedido'] = p1.pedido
        self.__pedido['cliente'] = novo_cliente.nome, novo_cliente.endereco
        self.__pedido['status'] = "Pedido realizado"
        self.__pedido['codigo'] = random.randrange(1,900)
        self.__pedidos.append(self.__pedido)
        print(self.__pedido.values())

    def registra_pedido_cadastrado(self, p1: Pedido, c1):
        self.__pedido['cliente'] = c1
        self.__pedido['pedido'] = p1.pedido
        self.__pedido['status'] = "Pedido realizado"
        self.__pedido['codigo'] = random.randrange(1,900)
        self.__pedidos.append(self.__pedido)
    
    def ver_pedidos(self):
        if self.__pedidos:
            print(('\n{}').format(self.__pedidos))
        else: print("Nao existem pedidos.")
        return False
    
    def ver_clientes(self):
        if self.__clientes:
            print(("\n{}").format(self.__clientes))
        else: print("Nao existem clientes cadastrados.")

    def mostra_tela_cadastro(self):
        nome = self.__tela_cliente.cadastro()
        return nome
    
    def voltar_tela_inicial(self):
        self.__controlador_transferencia.transferir()
            
    def sair(self):
        exit(0)