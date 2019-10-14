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
            "5: realizar pedido e cadastrar \n \n",
            "6: realizar pedido em um cadastro existente \n\n"
            "7: Cancelar o pedido atual e voltar para tela inicial \n\n"
            "0: para sair \n"
        )
        opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 6, 7, 0])
        return opcao

    def sair(self):
        exit(0)