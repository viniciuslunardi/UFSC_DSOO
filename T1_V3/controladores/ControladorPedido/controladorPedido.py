from entidades.pedido import Pedido
from telas.telaPedido import TelaPedido
from excecoes.naoTemPedidoException import NaoTemPedido
from datetime import datetime
from controladores.ControladorPedido.pedido_db import PedidoDB
pedido_db = PedidoDB('./controladores/ControladorPedido/pedido.db')
class ControladorPedido:
    def __init__(self, controlador_principal):
        self.__pedidos = []
        self.__pedidos_abertos = []
        self.__pedidos_fechados = []
        self.__controlador_principal = controlador_principal
        self.__main_view = TelaPedido()

    def cria_pedido(self, cliente):
        p1 = Pedido()
        self.monta_prato(p1, cliente)
        
    def monta_prato(self, pedido: Pedido, cliente):
        botoes, dados = self.__main_view.open()
        if botoes == 'Adicionar feijao':
            pedido.feijao()
        if botoes == 'Adicionar arroz':
            pedido.arroz()
        if botoes == 'Adicionar macarrao':
            pedido.macarrao()
        if botoes == 'Adicionar carne':
            pedido.carne()
        if botoes == 'Finalizar Pedido':
            self.finaliza(pedido, cliente)
    
    
    def finaliza(self, pedido, cliente):
        pedido_completo = {}
        keys = ['CLIENTE NOME', 'CPF', 'ENDERECO', 'PEDIDO', 'STATUS', 'CODIGO', 'DATA']
        values = [cliente.nome, cliente.cpf, cliente.endereco, 
        pedido.pedido, "Pedido realizado", len(self.__pedidos)+1, datetime.today()]
        for i in range(7):
            pedido_completo[keys[i]] = values[i]
        self.__pedidos.append(pedido_completo)
        self.__main_view.show_msg('SUCESSO', 'Pedido adicionado com sucesso')

    def ve_pedidos(self):
        try:
            if self.__pedidos:
                self.__main_view.show_msg("Pedidos", self.__pedidos)
            else: 
                raise NaoTemPedido
        except NaoTemPedido:
            self.__main_view.show_msg('ERROR', 'NAO TEM PEDIDOS')

    def ve_pedido_cliente(self, cliente):
        if self.__pedidos:
            for i in self.__pedidos:
                if i['CPF'] == cliente.cpf:
                    self.__main_view.show_msg('Pedidos', i)
            self.__main_view.show_msg('ERROR', 'Voce nao possui pedidos.')

    def ve_pedidos_fechados(self):
        if self.__pedidos_fechados:
            for i in self.__pedidos_fechados:
                self.__main_view.show_msg('Pedidos', str(i))
        else:
            self.__main_view.show_msg('Pedidos', 'Nao existem pedidos excluidos')

    def exclui_pedido(self, codigo):
        for pedido in self.__pedidos:
            if pedido['CODIGO'] == codigo:
                self.__pedidos_excluidos = list(filter(lambda i: i['CODIGO'] == codigo, self.__pedidos))
                self.__pedidos = list(filter(lambda i: i['CODIGO'] != codigo, self.__pedidos))
                self.__main_view.show_msg('SUCESSO', 'Exclusao feita com sucesso')
        self.__main_view.show_msg('ERROR', 'Nao foi possivel localizar o pedido')  

    def altera_status_pedido(self, codigo, status):
        for pedido in self.__pedidos:
            if pedido['CODIGO'] == codigo:
                pedido['STATUS'] = status
                self.__main_view.show_msg('Pedidos', 'Pedido atualizado com sucesso') 
        self.__main_view.show_msg('ERROR', 'Nao foi possivel localizar o pedido') 

    def exit(self):
        exit(0)
        