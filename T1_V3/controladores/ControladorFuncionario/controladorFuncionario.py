from entidades.funcionario import Funcionario
from telas.telaFuncionario import TelaFuncionario
class ControladorFuncionario:
    def __init__(self, controlador_principal):
        self.__funcionarios = []
        self.__controlador_principal = controlador_principal
        self.__main_view = TelaFuncionario()
    
    def entrou_funcionario(self):
        eventos, dados = self.__main_view.open()
        if eventos == 'Cadastrar cliente':
            self.inclui_cliente()
        elif eventos == 'Excluir cliente':
            self.exclui_cliente()
        elif eventos == 'Ver clientes':
            self.ve_clientes()
        elif eventos == 'Ver clientes excluidos':
            self.ve_clientes_excluidos()
        elif eventos == 'Ver pedidos':
            self.ve_pedidos()
        elif eventos == 'Ver pedidos excluidos':
            self.ve_pedidos_excluidos()
        elif eventos == 'Alterar pedido':
            self.altera_status_pedido()
        elif eventos == 'Excluir pedido':
            self.exclui_pedido()
        else:
            self.sair()

    def inclui_cliente(self):
        self.__controlador_principal.inclui_cliente()

    def exclui_cliente(self):
        botao, cpf = self.__main_view.open_cpf()
        if botao == 'Ok':
            self.__controlador_principal.exclui_cliente(int(cpf[0]))

    def ve_clientes(self):
        self.__controlador_principal.ve_clientes()

    def ve_clientes_excluidos(self):
        self.__controlador_principal.ve_clientes_excluidos()

    def ve_pedidos(self):
        self.__controlador_principal.ve_pedidos()
        
    def exclui_pedido(self):
        botao, pedido = self.__main_view.open_pedido()
        if botao == 'Ok':
            self.__controlador_principal.exclui_pedido(int(pedido[0]))

    def altera_status_pedido(self):
        botao, pedido = self.__main_view.open_pedido_status()
        if botao == 'Ok':
            self.__controlador_principal.altera_status_pedido(int(pedido[0]), pedido[1])

    def ve_pedidos_excluidos(self):
        self.__controlador_principal.ve_pedidos_excluidos()

    def sair(self):
        exit(0)