from controladores.controladorCliente import ControladorCliente
from controladores.controladorPedido import ControladorPedido
from controladores.controladorFuncionario import ControladorFuncionario
from telas.telaPrincipal import TelaPrincipal
class ControladorPrincipal:
    def __init__(self):
        self.__pedidos = []
        self.__pedidos_abertos = []
        self.__pedidos_fechados = []
        self.__pedidos_excluidos = []
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
        pedido = self.__controlador_pedidos.cria_pedido()
        pedido_completo = {}
        keys = ['CLIENTE NOME', 'CPF', 'ENDERECO', 'PEDIDO', 'STATUS', 'CODIGO']
        values = [cliente.nome, cliente.cpf, cliente.endereco, 
        (pedido), "Pedido realizado", len(self.__pedidos)+1]
        for i in range(6):
            pedido_completo[keys[i]] = values[i]
        self.__pedidos.append(pedido_completo)
        print("Pedido criado com sucesso.")
        self.__controlador_cliente.entrou_cliente()

    def ve_pedido_cliente(self, cliente):
        if self.__pedidos:
            for i in self.__pedidos:
                if i['CPF'] == cliente.cpf:
                    print(i)

    def ve_pedidos(self):
        if self.__pedidos:
            for i in self.__pedidos:
                print(i)
        else:
            print(
                "---------ATENCAO-----------\n"
                "Nao existem pedidos abertos\n"
            )

    def ve_pedidos_excluidos(self):
        if self.__pedidos_excluidos:
            for i in self.__pedidos_excluidos:
                print(i)
        else:
            print(
                "---------ATENCAO-----------\n"
                "Nao existem pedidos excluidos\n"
            )

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
        for pedido in self.__pedidos:
            if pedido['codigo'] == codigo:
                self.__pedidos_excluidos = list(filter(lambda i: i['codigo'] == codigo, self.__pedidos))
                self.__pedidos = list(filter(lambda i: i['codigo'] != codigo, self.__pedidos))
                print("Exclusao feita com sucesso")    

    def exclui_cliente(self):
        self.__controlador_cliente.exclui_cliente()

    def altera_status_pedido(self, codigo):
        for pedido in self.__pedidos:
            if pedido['CODIGO'] == codigo:
                pedido['STATUS'] = self.__controlador_funcionario.novo_status()
                print("Pedido atualizado com sucesso.")

    def exit(self):
        exit(0)