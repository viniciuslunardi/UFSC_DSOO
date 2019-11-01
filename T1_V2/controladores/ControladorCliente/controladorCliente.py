from telas.telaCliente import TelaCliente
from telas.telaClienteGUI import GUICliente
from entidades.endereco import Endereco
from entidades.cliente import Cliente
from excecoes.jaExisteClienteException import JaTemCliente
class ControladorCliente():
    __instance=None
    def __init__(self, controlador_principal):
        self.__clientes = []
        self.__clientes_excluido = []
        self.__cliente_atual = None
        self.__controlador_principal = controlador_principal
        self.__tela_cliente = TelaCliente(self)

    def entrou_cliente(self):
        switcher = {
            0: self.sai,
            1: self.__controlador_principal.cria_pedido,
            2: self.__controlador_principal.ve_pedido_cliente,
            3: self.altera_cliente,
            9: self.__controlador_principal.login
        }
        while True: 
            opcao = self.__tela_cliente.mostra_tela_cliente()
            funcao_escolhida = switcher[opcao]
            if opcao == int(1) or opcao == int(2):
                funcao_escolhida(self.__cliente_atual)
            else:
                funcao_escolhida()
    
    def altera_cliente(self):
        swithcer = {
            1: self.altera_nome,
            2: self.altera_cpf
        }
        opcao = self.__tela_cliente.mostra_tela_alteracao()
        funcao_escolhida = swithcer[opcao]
        funcao_escolhida()

    def altera_nome(self):
        nome = self.__tela_cliente.altera_nome()
        for cliente in self.__clientes:
            if cliente == self.__cliente_atual:
                cliente.nome = nome
                print("\nNome alterado com sucesso.")
    
    def altera_cpf(self):
        cpf = self.__tela_cliente.altera_cpf()
        for cliente in self.__clientes:
            if cliente == self.__cliente_atual:
                cliente.cpf = cpf
                print("\nCPF alterado com sucesso.")
        
    def inclui_cliente(self):
        novo_cliente = self.run()
        try:
            if self.existe_cliente(novo_cliente):
                raise JaTemCliente
            else: 
                self.__clientes.append(novo_cliente)
                GUICliente().cliente_cadastrado()
                print(
                    "\n Cliente cadastrado com sucesso.\n"
                )
                return novo_cliente
        except JaTemCliente:
            print("\n ------------ATENCAO------------\n")
            print("Nao eh possivel cadastrar clientes com o mesmo cpf.\n")
            return GUICliente().ja_tem_cliente()

    def exclui_cliente(self):
        cpf = int(self.__tela_cliente.mostra_tela_exclusao_cliente())
        try:
            for cliente in self.__clientes:
                if cliente.cpf == cpf:
                    self.__clientes_excluido.append(cliente)
            self.__clientes = list(filter(lambda i: i.cpf != cpf, self.__clientes))
            print("\n Cliente excluido com sucesso.\n")
        except Exception:
            print(
                "-----------------ATENCAO---------------\n"
                "Nao existem clientes com esse cpf.\n"
            )   

    def existe_cliente(self, c1):
        for clientes in self.__clientes:
            if clientes == c1:
                return True
        return False
                
    def ve_clientes(self):
        if self.__clientes:
            for cliente in self.__clientes:
                print(cliente)
        else:
            print(
                "\n------------AtENCAO----------\n"
                "Nao existem clientes cadastrados.\n"
            )

    def escolhe_cliente(self, cpf: int):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                self.__cliente_atual = cliente
                return cliente
        return False
    
    def ve_clientes_excluidos(self):
        if self.__clientes_excluido:
            for cliente in self.__clientes_excluido:
                print(cliente)

    def run(self):
        botao, dados = GUICliente().open()
        novo_end = Endereco(dados[6], dados[3], dados[4], dados[5])
        novo_cliente = Cliente(dados[0], int(dados[1]), dados[2], novo_end)
        return novo_cliente

    def sai(self):
        exit(0)
