from telas.telaCliente import TelaCliente
from entidades.endereco import Endereco
from entidades.cliente import Cliente
class ControladorCliente():
    def __init__(self, controlador_principal):
        self.__clientes = []
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
        novo_cliente = self.__tela_cliente.cadastro()
        try:
            if self.existe_cliente(novo_cliente):
                raise Exception
            else: 
                self.__clientes.append(novo_cliente)
                print(
                    "\n Cliente cadastrado com sucesso.\n"
                )
                return novo_cliente
        except Exception:
            print("\n ------------ATENCAO------------\n")
            print("Nao eh possivel cadastrar clientes com o mesmo cpf.\n")

    def exclui_cliente(self):
        cpf = int(self.__tela_cliente.mostra_tela_exclusao_cliente())
        try:
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
    def sai(self):
        exit(0)
