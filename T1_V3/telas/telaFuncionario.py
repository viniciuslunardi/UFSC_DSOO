import PySimpleGUI as sg
class TelaFuncionario:
    def __init__(self):
        self.__window = None
        self.__window_cpf = None
        self.__window_pedido = None
        self.__window_pedido_status = None
        self.init_components()

    def init_components(self):
        layout = [
 		[sg.Text('Ola, seja bem vindo!')],
		[sg.Text('Escolha a opcao desejada: ')],
        [sg.Button('Cadastrar cliente'), sg.Button('Excluir cliente'), sg.Button('Ver clientes'),
        sg.Button('Ver clientes excluidos')], 
        [sg.Button('Ver pedidos'), sg.Button('Excluir pedido'), 
        sg.Button('Alterar pedido'), sg.Button('Ver pedidos excluidos')], 
        [sg.Button('Sair')]
 		]
        self.__window = sg.Window('Larikas', default_element_size=(50,20)).Layout(layout)
        
        layout_cpf = [
            [sg.Text('Digite o cpf do cliente'), sg.In()],
            [sg.Button('Ok'), sg.Button('Cancelar')]
        ]
        self.__window_cpf = sg.Window('Exclusao cliente', default_element_size=(50,20)).Layout(layout_cpf)

        layout_pedido = [
            [sg.Text('Digite o codigo do pedido'), sg.In()],
            [sg.Button('Ok'), sg.Button('Cancelar')]
        ]
        self.__window_pedido = sg.Window('Alteracao pedido', default_element_size=(50,20)).Layout(layout_pedido)

        layout_pedido_status = [
            [sg.Text('Digite o codigo do pedido e o novo status'), sg.In(), sg.In('Status')],
            [sg.Button('Ok'), sg.Button('Cancelar')]
        ]
        self.__window_pedido_status = sg.Window('Alteracao pedido', default_element_size=(50,20)).Layout(layout_pedido_status)

    def open(self):
        while True:    
            eventos, dados = self.__window.Read()
            return eventos, dados
        self.__window.Close()

    def open_cpf(self):
        eventos, dados = self.__window_cpf.Read()
        self.__window_cpf.Close()
        return eventos, dados

    def open_pedido(self):
        eventos, dados = self.__window_pedido.Read()
        self.__window_pedido.Close()
        return eventos, dados
    
    def open_pedido_status(self):
        eventos, dados = self.__window_pedido_status.Read()
        self.__window_pedido_status.Close()
        return eventos, dados

    def show_msg(self, title: str, msg: str):
        sg.Popup(title, msg)