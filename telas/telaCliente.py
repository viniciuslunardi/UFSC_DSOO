from entidades.endereco import Endereco
from entidades.cliente import Cliente
class TelaCliente:
    def __init__(self, controlador):
        self.__controlador = controlador
        
    def escolhe_cliente(self):
        cpf = self.le_numero_inteiro("Digite seu cpf: ")
        return cpf

    def mostra_tela_exclusao_cliente(self):
        print(
            "\n---------------ATENCAO----------\n"
            "Para excluir um cliente sera necessario \n"
            "Seu numero de cpf. \n"
        )
        opcao = self.le_numero_inteiro("Digite o cpf do cliente: ")
        return str(opcao) 

    def cadastro(self):
        print(
            "Para cadastrar um cliente sera necessario de alguns dados \n"
            "Sao eles: Nome, Cpf, Telefone, Endereco: Rua, numero, complemento e cep"
        )
        opcao = self.le_cadastro()
        return opcao

    def le_cadastro(self):
        nome = str(input("Digite o nome do cliente: "))
        cpf = int(input("Digite o cpf do cliente: "))
        telefone = str(input("Digite o telefone do cliente: "))
        rua = str(input("Digite o nome da rua do cliente: "))
        try:
            numero = int(input("Digite o numero do endereco do cliente: "))
        except Exception:
            numero = input("Voce deve inserir so e somente so numeros: ")         
        complemento = str(input("Digite o complemento do endereco do cliente: "))
        cep = str(input("Digite o cep do cliente: "))
        e1 = Endereco(cep, rua, numero, complemento)
        c1 = Cliente(nome, cpf, telefone, e1)
        return c1

    def le_numero_inteiro(self, msg: str="", lista_valida = []):
        while True:
            try:
                inteiro = int(input(msg))
                if lista_valida and inteiro not in lista_valida:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto: Digite um valor valido.")
                if lista_valida:
                    print("Valores validos: ", lista_valida)

    def mostra_tela_cliente(self):
        print(
            "\n ---------------Ola------------------- \n \n",
            "Para fazer um novo pedido digite: 1 \n \n",
            "Para ver seus pedidos digite: 2 \n \n",
            "Para alterar algum dado digite: 3 \n\n",
            "Para voltar para tela inicial digite: 9 \n \n",
            "Para sair digite: 0 \n"
        )
        opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 3, 9, 0])
        if opcao == 0:
            self.sair()
        return opcao
    
    def mostra_tela_alteracao(self):
        print(
            "\n------------------ATENCAO-----------------\n\n"
            "Para alterar o nome do cliente digite: 1 \n\n"
            "Para alterar o cpf do cliente digite: 2 \n\n"
            "Para sair digite: 0\n"
        )
        opcao = self.le_numero_inteiro("Escolha o atributo que deseja alterar: ", [1,2,3,4,5,0])
        return opcao

    def altera_cpf(self):
        cpf = int(input("Digite o cpf: "))
        return cpf

    def altera_nome(self):
        nome = str(input("Digite o nome: "))
        return nome

    def sair(self):
        exit(0)