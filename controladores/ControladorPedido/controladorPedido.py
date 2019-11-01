from entidades.pedido import Pedido
from telas.telaPedido import TelaPedido
from excecoes.naoTemPedidoException import NaoTemPedido
from datetime import datetime
class ControladorPedido:
    def __init__(self, controlador_principal):
        self.__nao_tem_pedido = NaoTemPedido()
        self.__pedidos = []
        self.__pedidos_abertos = []
        self.__pedidos_fechados = []
        self.__controlador_principal = controlador_principal
        self.__tela_pedido = TelaPedido(self)

    def cria_pedido(self, cliente):
        p1 = Pedido()
        while True:
            self.monta_prato(p1, cliente)
        return False
        
    def monta_prato(self, pedido: Pedido, cliente):
        opcoes = {1: pedido.arroz, 2: pedido.feijao, 3: pedido.macarrao, 
        4: pedido.carne, 5: self.finaliza, 0: self.exit}
        opcao = self.__tela_pedido.mostra_tela_opcoes()
        funcao_escolhida = opcoes[opcao]    
        if opcao == int(5):
            return funcao_escolhida(pedido, cliente)   
        else: funcao_escolhida()

    def finaliza(self, pedido, cliente):
        pedido_completo = {}
        keys = ['CLIENTE NOME', 'CPF', 'ENDERECO', 'PEDIDO', 'STATUS', 'CODIGO', 'DATA']
        values = [cliente.nome, cliente.cpf, cliente.endereco, 
        (pedido), "Pedido realizado", len(self.__pedidos)+1, datetime.today()]
        for i in range(7):
            pedido_completo[keys[i]] = values[i]
        self.__pedidos.append(pedido_completo)
        print("Pedido criado com sucesso.")
        self.__controlador_principal.volta_cliente()
        return False

    def ve_pedidos(self):
        try:
            if self.__pedidos:
                for i in self.__pedidos:
                    print(i)
            else: 
                raise NaoTemPedido
        except NaoTemPedido:
            print(self.__nao_tem_pedido)

    def ve_pedido_cliente(self, cliente):
        if self.__pedidos:
            for i in self.__pedidos:
                if i['CPF'] == cliente.cpf:
                    print(i)

    def ve_pedidos_fechados(self):
        if self.__pedidos_fechados:
            for i in self.__pedidos_fechados:
                print(i)
        else:
            print(
                "---------ATENCAO-----------\n"
                "Nao existem pedidos fechados\n"
            )

    def exclui_pedido(self, codigo):
        for pedido in self.__pedidos:
            if pedido['CODIGO'] == codigo:
                self.__pedidos_excluidos = list(filter(lambda i: i['CODIGO'] == codigo, self.__pedidos))
                self.__pedidos = list(filter(lambda i: i['CODIGO'] != codigo, self.__pedidos))
                print("Exclusao feita com sucesso")    

    def altera_status_pedido(self, codigo, status):
        for pedido in self.__pedidos:
            if pedido['CODIGO'] == codigo:
                pedido['STATUS'] = status
                print("Pedido atualizado com sucesso.")

    def exit(self):
        exit(0)
        