from controladores.ControladorCliente.controladorCliente import ControladorCliente
from controladores.ControladorPedido.controladorPedido import ControladorPedido
from controladores.ControladorFuncionario.controladorFuncionario import ControladorFuncionario
from telas.telaPrincipal import TelaPrincipal
class ControladorPrincipal:
    def __init__(self):
        self.__main_view = TelaPrincipal()
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_pedidos = ControladorPedido(self)
    
    def entra_cliente(self):
        self.__controlador_cliente.autenticar()

    def cria_pedido(self, cliente):
        self.__controlador_pedidos.cria_pedido(cliente)

    def volta_cliente(self):
        self.__controlador_cliente.entrou_cliente()

    def ve_pedido_cliente(self, cliente):
        self.__controlador_pedidos.ve_pedido_cliente(cliente)

    def ve_pedidos(self):
        self.__controlador_pedidos.ve_pedidos()

    def ve_pedidos_excluidos(self):
        self.__controlador_pedidos.ve_pedidos_fechados()

    def ve_clientes(self):
        self.__controlador_cliente.ve_clientes()

    def entra_funcionario(self):
        self.__controlador_funcionario.entrou_funcionario()

    def exclui_pedido(self, codigo: int):
        self.__controlador_pedidos.exclui_pedido(codigo)

    def exclui_cliente(self, cpf: int):
        self.__controlador_cliente.exclui_cliente(cpf)

    def ve_clientes_excluidos(self):
        self.__controlador_cliente.ve_clientes_excluidos()

    def altera_status_pedido(self, codigo, status):
        self.__controlador_pedidos.altera_status_pedido(codigo, status)

    def inclui_cliente(self):
        self.__controlador_cliente.inclui_cliente()

    def run(self):
        eventos, dados = self.__main_view.open()
        if eventos =='Cancelar':
            self.__main_view.close()
        elif eventos == 'Entrar como funcionario':
            self.entra_funcionario()
        elif eventos == 'Entrar como cliente': 
            self.entra_cliente()
        elif eventos == 'Cadastrar cliente':
            self.inclui_cliente()
 
    def exit(self):
        exit(0)
