import PySimpleGUI as sg
class TelaCliente:
    def __init__(self):
        self.__window = None
        self.__window_cadastro = None
        self.__window_login = None
        self.__window_nome = None
        self.__window_cpf = None
        self.__window_senha = None
        self.init_components()

    def init_components(self):
        layout = [
 		[sg.Text('Ola, seja bem vindo!', justification='center', font=("Helvetica", 25))],
		[sg.Text('Escolha a opcao desejada: ', font=("Helvetica", 20))],
        [sg.Button('Fazer novo pedido'), sg.Button('Ver pedidos')], 
        [sg.Button('Mudar nome'), sg.Button('Mudar cpf'), sg.Button('Mudar senha')], 
        [sg.Button('Ver dados'), sg.Button('Sair')]
 		]
        self.__window = sg.Window('Larikas', default_element_size=(50,20)).Layout(layout)
        layout2 = [
 		[sg.Text('Por favor digite seu: Nome, CPF, Telefone, Endereco')],
		[sg.Text('Nome', size=(15, 1)), sg.InputText()],
		[sg.Text('CPF', size=(15, 1)), sg.Input()],
		[sg.Text('Telefone', size=(15, 1)), sg.InputText()],
		[sg.Text('Rua', size=(15, 1)), sg.InputText()],
		[sg.Text('Numero', size=(15, 1)), sg.InputText()],
		[sg.Text('Complemento', size=(15, 1)), sg.InputText()],
		[sg.Text('Cep', size=(15, 1)), sg.InputText()],
		[sg.Button('Cadastrar'), sg.Button('Cancelar')]
 		]
        self.__window_cadastro = sg.Window('Larikas Cadastro', default_element_size=(50,20)).Layout(layout2)
        
        layout3= [
            [sg.Text('Digite seu cpf e sua senha para se autenticar')],
            [sg.Text('CPF'), sg.In(),],
            [sg.Text('SENHA'), sg.In(password_char='*')],
            [sg.Submit('Entrar'), sg.Cancel('Cancelar')]
        ]
        self.__window_login = sg.Window('Autenticacao Larikas', default_element_size=(50,20)).Layout(layout3)
        
        layout_cpf = [
            [sg.Text('Digite o novo cpf'), sg.In()],
            [sg.Button('Alterar'), sg.Button('Cancelar')]
        ]
        self.__window_cpf = sg.Window('Alteracao cadastro', default_element_size=(50,20)).Layout(layout_cpf)
        
        layout_nome = [
            [sg.Text('Digite o novo nome'), sg.InputText()],
            [sg.Button('Alterar'), sg.Button('Cancelar')]
        ]
        
        self.__window_nome = sg.Window('Alteracao cadastro', default_element_size=(50,20)).Layout(layout_nome)
        
        layout_senha = [
            [sg.Text('Digite a nova senha'), sg.In(password_char='*')],
            [sg.Button('Alterar'), sg.Button('Cancelar')]
        ]
        self.__window_senha = sg.Window('Alteracao cadastro', default_element_size=(50,20)).Layout(layout_senha)

    def open(self):
        while True:
            eventos, dados = self.__window.Read()
            return eventos, dados
        self.__window.Close()
        
    def open_cadastro(self):
        while True:
            eventos, dados = self.__window_cadastro.Read()
            if eventos == 'Cadastrar':
                try:
                    dados[1] = int(dados[1])
                    dados[4] = int(dados[4])
                except:
                    if dados[0] == '':
                        self.show_msg('ERROR','Nome nao pode estar vazio')
                    elif isinstance(dados[1], str) or dados[1] == '':
                        self.show_msg('ERROR', 'CPF deve ser digitado somento com numeros')
                    elif dados[2] == '':
                        self.show_msg('ERROR','telefone nao pode estar vazio')
                    elif dados[3] == '':
                        self.show_msg('ERROR','Rua nao podem estar vazio')
                    elif isinstance(dados[4], str) or dados[4] == '':
                        self.show_msg('ERROR', 'Numero da casa deve ser somento numeros')
                    elif dados[5] == '':
                        self.show_msg('ERROR','Complemento nao podem estar vazio')
                    elif isinstance(dados[1], int) and isinstance(dados[4], int):
                        self.close_cadastro()
                        return eventos, dados
                else:
                    return eventos, dados
            elif eventos == 'Cancelar':
                self.close_cadastro()
                False
            return eventos, dados
    
    def open_login(self):
        while True:
            eventos, dados = self.__window_login.Read()
            self.close_login()
            return eventos, dados
        
        
    def open_senha(self):
        eventos, dados = self.__window_senha.Read()
        self.__window_senha.Close()
        return eventos, dados
    
    def open_cpf(self):
        eventos, dados = self.__window_cpf.Read()
        self.__window_cpf.Close()
        return eventos, dados
    
    def open_nome(self):
        eventos, dados = self.__window_nome.Read()
        self.__window_nome.Close()
        return eventos, dados

    def close(self):
        self.__window.Close()

    def close_cadastro(self):
        self.__window_cadastro.Close() 

    def close_login(self):
        self.__window_login.Close()

    def show_msg(self, title: str, msg: str):
        sg.Popup(title, msg)