import PySimpleGUI as sg
class TelaPrincipal:
    def __init__(self):
        self.__window = None
        self.__login_cliente = None
        self.init_components()

    def init_components(self):
        layout = [
 		[sg.Text('Ola, seja bem vindo!')],
		[sg.Text('Escolha a opcao desejada: ')],
        [sg.Button('Entrar como cliente'), sg.Button('Entrar como funcionario'), sg.Button('Cadastrar cliente')],
        [sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Larikas', default_element_size=(500,20)).Layout(layout)
        layout2 = [
            [sg.Text('Digite o cpf do cliente para entrar'), sg.Input()],
            [sg.Submit('OK')]
        ]
        self.__login_cliente = sg.Window('Larikas login', default_element_size=(50,20)).Layout(layout2)


    def open(self):
        eventos, dados = self.__window.Read()
        self.close()
        return eventos, dados

    def open_cliente(self):
        botao, dados = self.__login_cliente.Read()
        self.close()
        return botao, dados

    def close(self):
        self.__window.Close()