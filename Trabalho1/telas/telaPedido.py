class TelaPedido:
    def __init__(self, controlador):
        self.__controlador = controlador

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
                    
    def mostra_tela_opcoes(self):
        print(
            "Digite a opção desejada para adicionar ao seu pedido. \n \n",
            "1: arroz \n \n",
            "2: feijao \n \n",
            "3: macarrao \n \n",
            "4: carne \n \n",
            "5: realizar pedido \n \n",
            "0: para sair \n"
        )
        opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 0])
        return opcao
    
    def mostra_tela_cliente(self):
        print(
            "\n ---------------Ola------------------- \n \n",
            "Para fazer um novo pedido digite: 1 \n \n",
            "Para ver seus pedidos digite: 2 \n \n",
            "Para cancelar o pedido digite: 9 \n \n",
            "Para sair digite: 0 \n"
        )
        opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 9, 0])
        if opcao == 0:
            self.sair()
        return opcao


    def sair(self):
        exit(0)