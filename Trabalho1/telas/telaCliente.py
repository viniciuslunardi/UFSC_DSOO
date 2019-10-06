from entidades.endereco import Endereco
from entidades.cliente import Cliente
class TelaCliente:
    def __init__(self, controlador):
        self.__controlador = controlador
   
    def cadastro(self):
        print(
            "Para cadastrar um cliente sera necessario de alguns dados \n"
            "Sao eles: Nome, Cpf, Telefone, Endereco: Rua, numero, complemento e cep"
        )
        opcao = self.le_cadastro()
        print()
        print("Cliente cadastrado com sucesso.")
        return opcao

    def le_cadastro(self):
        nome = str(input("Digite o nome do cliente: "))
        cpf = str(input("Digite o cpf do cliente: "))
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
            valor_lido = input(msg)
            try:
                inteiro = int(valor_lido)
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
            "Para entrar como funcionario digite: 9 \n \n",
            "Para sair digite: 0 \n"
        )
        opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 9, 0])
        if opcao == 0:
            self.sair()
        return opcao
    
    def sair(self):
        exit(0)