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
        self.carrega_pedido()
        self.__main_view = TelaPedido()

    def carrega_pedido(self):
        rows = pedido_db.fetch()
        for pedido in rows:
            pedido_completo = {}
            keys = ['NOME', 'CPF', 'TELEFONE', 'RUA', 'NUMERO', 'COMPLEMENTO', 'PEDIDO', 'DATA', 'STATUS', 'CODIGO']
            values = [pedido[1], pedido[2], pedido[3], pedido[4], pedido[5], 
            pedido[6], pedido[7], pedido[8], pedido[9], pedido[0]]
            for i in range(10):
                pedido_completo[keys[i]] = values[i]
            self.__pedidos.append(pedido_completo)
    
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
        if botoes == 'Finalizar pedido':
            for dado in dados:
                if dado == 'Adicionar feijao':
                    pedido.feijao()
                if dado == 'Adicionar arroz':
                    pedido.arroz()
                if dado == 'Adicionar macarrao':
                    pedido.macarrao()
                if dado == 'Adicionar carne':
                    pedido.carne()
            self.finaliza(pedido, cliente)
       
    def finaliza(self, pedido, cliente):
        pedido_completo = {}
        keys = ['NOME', 'CPF', 'TELEFONE', 'RUA', 'NUMERO', 'COMPLEMENTO',
         'PEDIDO', 'STATUS', 'DATA', 'CODIGO']
        values = [cliente.nome, cliente.cpf, cliente.telefone, cliente.rua, cliente.numero, 
        cliente.complemento, pedido.pedido, "Pedido realizado", datetime.today(), 
        len(self.__pedidos)+1]
        for i in range(10):
            pedido_completo[keys[i]] = values[i]
        self.__pedidos.append(pedido_completo)
        pedido_db.insert(
            pedido_completo['CODIGO'], pedido_completo['NOME'], pedido_completo['CPF'],
            pedido_completo['TELEFONE'], cliente.rua, cliente.numero, 
            cliente.complemento, str(pedido_completo['PEDIDO']), 
            str(pedido_completo['DATA']), pedido_completo['STATUS']
            )
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
            lista = []
            for i in self.__pedidos:
                if i['CPF'] == cliente.cpf:
                    lista.append(i)
            self.__main_view.show_msg('Pedidos', lista)

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
                pedido_db.remove(pedido['CODIGO'])
                self.__pedidos = list(filter(lambda i: i['CODIGO'] != codigo, self.__pedidos))
                self.__main_view.show_msg('SUCESSO', 'Exclusao feita com sucesso')
        self.__main_view.show_msg('ERROR', 'Nao foi possivel localizar o pedido')  

    def altera_status_pedido(self, codigo, status):
        for pedido in self.__pedidos:
            if pedido['CODIGO'] == int(codigo):
                pedido['STATUS'] = status
                pedido_db.update(pedido['CODIGO'], pedido['NOME'], pedido['CPF'], pedido['TELEFONE'],
                 pedido['RUA'], pedido['NUMERO'], pedido['COMPLEMENTO'], pedido['PEDIDO'], pedido['STATUS'], pedido['DATA'])
                self.__main_view.show_msg('Pedidos', 'Pedido atualizado com sucesso') 
        self.__main_view.show_msg('ERROR', 'Nao foi possivel localizar o pedido') 

    def exit(self):
        exit(0)
        