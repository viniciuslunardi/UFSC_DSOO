from controladores.ControladorCliente.controladorCliente import ControladorCliente
from controladores.ControladorPedido.controladorPedido import ControladorPedido
from controladores.ControladorFuncionario.controladorFuncionario import ControladorFuncionario
from telas.telaPrincipal import TelaPrincipal
class ControladorPrincipal:
    def __init__(self):
        self.__tela_principal = TelaPrincipal(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_pedidos = ControladorPedido(self)

    def login(self):
        switcher = {
            0: self.exit,
            1: self.entra_cliente,
            2: self.entra_funcionario,
            3: self.cadastro
        }
        opcao = self.__tela_principal.boas_vindas()
        funcao_escolhida = switcher[opcao]
        funcao_escolhida()
    
    def entra_cliente(self):
        while True:
            identificador = self.__tela_principal.boas_vindas_cliente()
            if self.__controlador_cliente.escolhe_cliente(identificador):
                self.__controlador_cliente.entrou_cliente()
            else: print("Nao foi localizado um cliente com esse cpf.")

    def cria_pedido(self, cliente):
        while True:
            self.__controlador_pedidos.cria_pedido(cliente)

    def volta_cliente(self):
        self.__controlador_cliente.entrou_cliente()

    def ve_pedido_cliente(self, cliente):
        self.__controlador_pedidos.ve_pedido_cliente(cliente)

    def ve_pedidos(self):
        self.__controlador_pedidos.ve_pedidos()

    def ve_pedidos_fechados(self):
        self.__controlador_pedidos.ve_pedidos_fechados()

    def ve_clientes(self):
        return self.__controlador_cliente.ve_clientes()

    def cadastra_cliente(self):
        self.__controlador_cliente.inclui_cliente()

    def entra_funcionario(self):
        self.__controlador_funcionario.entrou_funcionario()

    def cadastro(self):
        self.__controlador_cliente.inclui_cliente()
        self.login()

    def exclui_pedido(self, codigo):
        self.__controlador_pedidos.exclui_pedido(codigo)

    def exclui_cliente(self):
        self.__controlador_cliente.exclui_cliente()

    def ve_clientes_excluidos(self):
        self.__controlador_cliente.ve_clientes_excluidos()

    def altera_status_pedido(self, codigo):
        status = self.__controlador_funcionario.novo_status()
        self.__controlador_pedidos.altera_status_pedido(codigo, status)

    def exit(self):
        exit(0)