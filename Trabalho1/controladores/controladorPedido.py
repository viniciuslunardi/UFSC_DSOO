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
        self.__tela_pedido = TelaPedido(self)
        self.__tela_funcionario = TelaFuncionario(self)
        self.__tela_cliente = TelaCliente(self)
        self.__tela_principal = TelaPrincipal(self)
    
    def cadastrar_cliente(self):
        dicts = {}
        novo_cliente = self.__tela_funcionario.mostra_tela_cadastro_cliente()
        values = [novo_cliente.nome, novo_cliente.cpf, novo_cliente.endereco, novo_cliente.telefone,
        len(self.__clientes)+1]
        keys = ['nome', 'cpf', 'endereco', 'telefone', 'codigo']
        for i in range(len(values)):
            dicts[keys[i]] = values[i]
        try:    
            if self.existe_cliente(novo_cliente.cpf):
                raise Exception
            else:     
                self.__clientes.append(dicts)
                print(('cliente {} cadastrado com sucesso.').format(novo_cliente.nome))
                return novo_cliente
        except Exception:
            print("Impossivel cadastrar clientes com o mesmo cpf!")

    def criar_pedido(self):
        p1 = Pedido()
        while True:
            self.editar_pedido(p1)
    
    def editar_pedido(self, pedido: Pedido):
        produtos = {1: pedido.arroz, 2: pedido.feijao, 3: pedido.macarrao, 
        4: pedido.carne, 5: self.registra_pedido_novo, 6: self.registra_pedido_cadastrado, 
        7: self.entrou_cliente, 0: self.__tela_pedido.sair}
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
        9: self.entrou_funcionario, 0: self.sair}
        while True: 
            opcao = self.__tela_cliente.mostra_tela_cliente()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
    
    def entrou_funcionario(self):
        switcher = {0: self.sair, 1: self.ver_pedidos, 2: self.cadastrar_cliente, 
        3: self.ver_clientes, 4: self.remove_pedido, 5: self.remove_cliente, 
        9: self.entrou_cliente}
        while True: 
            opcao = self.__tela_funcionario.mostra_tela_funcionario()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def registra_pedido_novo(self, p1: Pedido):
        dicts = {}
        novo_cliente = self.cadastrar_cliente()
        values = [novo_cliente.nome + str(novo_cliente.endereco), p1.pedido, "Pedido realizado", len(self.__pedidos)+1]
        keys = ['cliente', 'pedido', 'status', 'codigo']
        for i in range(len(values)):
            dicts[keys[i]] = values[i]
        self.__pedidos.append(dicts)
        print("Pedido realizado com sucesso.")

    def registra_pedido_cadastrado(self, p1: Pedido, c1):
        dicts = {}
        values = ['Rafael, (Rua protenor vidal, 237, ap 09)', p1.pedido, "Pedido realizado", len(self.__pedidos)+1]
        keys = ['cliente', 'pedido', 'status', 'codigo']
        for i in range(len(values)):
            dicts[keys[i]] = values[i]
        self.__pedidos.append(dicts)
        print("Pedido realizado com sucesso.")
    
    def ver_pedidos(self):
        if self.__pedidos:
            for i in range(len(self.__pedidos)):
                print(('\n{}').format(self.__pedidos[i]))
        else: print(
            "\n-------ATENCAO---------"
            "\nNao existem pedidos."
            )
    
    def ver_clientes(self):
        if self.__clientes:
            for i in range(len(self.__clientes)):
                print(self.__clientes[i])
        else: 
            print("Nao existem clientes cadastrados.")

    def mostra_tela_cadastro(self):
        nome = self.__tela_cliente.cadastro()
        return nome
    
    def existe_cliente(self, cliente: Cliente):
        if cliente not in self.__clientes:
            return False
        elif cliente in self.__clientes: 
            return True

    def remove_pedido(self):
        codigo = self.__tela_funcionario.mostra_tela_alteracao_pedido()
        try:
            self.__pedidos = list(filter(lambda i: i['codigo'] != codigo, self.__pedidos))
        except Exception:
            print("Oi")

    def remove_cliente(self):
        codigo = self.__tela_funcionario.mostra_tela_exclusao_cliente()
        try:
            if codigo in self.__clientes:
                self.__clientes = list(filter(lambda i: i['cpf'] != codigo, self.__clientes))
            else: raise Exception
        except Exception:
            print(
                "-----------------ATENCAO---------------\n"
                "Nao existem clientes com essa matricula\n"
            )   

    def sair(self):
        exit(0)