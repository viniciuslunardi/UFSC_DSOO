from entidades.funcionario import Funcionario
from telas.telaFuncionario import TelaFuncionario
class ControladorFuncionario:
    def __init__(self, controlador_principal):
        self.__funcionarios = []
        self.__controlador_principal = controlador_principal
        self.__tela_funcionario = TelaFuncionario(self)
    
    def entrou_funcionario(self):
        switcher = {
            0: self.sair,
            1: self.__controlador_principal.ve_pedidos,
            2: self.__controlador_principal.ve_clientes,
            3: self.__controlador_principal.cadastra_cliente,
            4: self.exclui_pedido,
            5: self.__controlador_principal.exclui_cliente,
            6: self.__controlador_principal.ve_pedidos_fechados,
            7: self.altera_status_pedido,
            8: self.__controlador_principal.ve_clientes_excluidos,
            9: self.__controlador_principal.login
        }
        while True:
            opcao = self.__tela_funcionario.mostra_tela_funcionario()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def exclui_pedido(self):
        pedido = self.__tela_funcionario.mostra_tela_exclusao_pedido()
        self.__controlador_principal.exclui_pedido(pedido)

    def altera_status_pedido(self):
        pedido = self.__tela_funcionario.mostra_tela_alteracao_pedido()
        self.__controlador_principal.altera_status_pedido(pedido)
    
    def novo_status(self):
        novo_status = self.__tela_funcionario.novo_status()
        return novo_status

    def sair(self):
        exit(0)