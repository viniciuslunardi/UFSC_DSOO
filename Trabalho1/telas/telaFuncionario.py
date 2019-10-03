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
            "\n ---------------Ola-------------------\n \n",
            "Digite 1 para ver todos os pedidos abertos\n \n"
            "Digite 0 para sair \n"
            "Teste"
        )
        opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 0])
        if opcao == 0:
            self.sair()
        return opcao
        
    def sair(self):
        exit(0)