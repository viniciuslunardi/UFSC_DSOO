class TelaPrincipal:
    def __init__(self, controlador):
        self.__controlador_restaurante = controlador

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

    def boas_vindas(self):
        print("----------------BEM VINDO AO RESTAURANTE----------------- \n")
        print("Se voce é um cliente - Digite 1 \n")
        print("Agora, se voce for um funcionario - Digite 2 \n")
        print("Para se cadastrar como cliente - Digite 3 \n")
        print("E se desejar sair - Digite 0 \n")
        opcao = self.le_numero_inteiro("Escolha uma das opcoes: ", [1, 2, 3, 0])
        return opcao

    def boas_vindas_cliente(self):
        print()
        print("Para entrar como cliente eh necessario informar o cpf cadastrado")
        opcao = self.le_numero_inteiro("Digite seu cpf: ")
        return (opcao)
    