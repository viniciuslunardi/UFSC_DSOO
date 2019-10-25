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
            9: self.__controlador_principal.login
        }
        while True:
            opcao = self.__tela_funcionario.mostra_tela_funcionario()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def sair(self):
        exit(0)