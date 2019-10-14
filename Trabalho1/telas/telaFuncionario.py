from entidades.endereco import Endereco
from entidades.cliente import Cliente
class TelaFuncionario:

    def __init__(self, controlador):
        self.__controlador_pedido = controlador
    
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
    
    def mostra_tela_funcionario(self):
        print(
            "\n ---------------Ola-------------------\n \n"
            "Digite 1 para ver todos os pedidos abertos\n \n"
            "Digite 2 para cadastrar um cliente novo \n\n"
            "Digite 3 para ver os clientes cadastrados \n\n"
            "Digite 4 para excluir um pedido \n\n"
            "Digite 5 para excluir um cliente \n\n"
            "Digite 9 para entrar como cliente \n\n"
            "Digite 0 para sair \n"
        )
        opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 9, 0])
        print()
        if opcao == 0:
            self.sair()
        return opcao
    
    def mostra_tela_alteracao_pedido(self):
        print(
            "\n -------------------------ATENCAO-------------------------------------"
            "\n Para remocao de um pedido sera necessario o codigo do mesmo.\n"
        )
        opcao = self.le_numero_inteiro("Digite o codigo do pedido: " )
        return opcao

    def mostra_tela_cadastro_cliente(self):
        print(
            "Para cadastrar um cliente sera necessario de alguns dados \n"
            "Sao eles: Nome, Cpf, Telefone, Endereco: Rua, numero, complemento e cep"
        )
        opcao = self.le_cadastro()
        return opcao

    def le_cadastro(self):
        nome = str(input("Digite o nome do cliente: "))
        cpf = str(input("Digite o cpf do cliente: "))
        telefone = str(input("Digite o telefone do cliente: "))
        rua = str(input("Digite o nome da rua do cliente: "))
        numero = int(input("Digite o numero do endereco do cliente: "))
        complemento = str(input("Digite o complemento do endereco do cliente: "))
        cep = str(input("Digite o cep do cliente: "))
        e1 = Endereco(cep, rua, numero, complemento)
        c1 = Cliente(nome, cpf, telefone, e1)
        return c1
    
    def mostra_tela_exclusao_cliente(self):
        print(
            "\n---------------ATENCAO----------\n\n"
            "Para excluir um cliente sera necessario \n"
            "Seu codigo de matricula ou cpf \n"
        )
        opcao = self.le_numero_inteiro("Digite a matricula do cliente: \n")
        return opcao

    def sair(self):
        exit(0)