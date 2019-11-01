import PySimpleGUI as sg

class GUICliente:
	def __init__(self):
		self.__window = None
		self.init_components()

	def init_components(self):
		layout = [
 		[sg.Text('Por favor digite seu: Nome, CPF, Telefone, Endereco')],
		[sg.Text('Nome', size=(15, 1)), sg.InputText('Nome')],
		[sg.Text('CPF', size=(15, 1)), sg.InputText('CPF')],
		[sg.Text('Telefone', size=(15, 1)), sg.InputText('Telefone')],
		[sg.Text('Rua', size=(15, 1)), sg.InputText('Endereco.RUA')],
		[sg.Text('Numero', size=(15, 1)), sg.InputText('Endereco.NMR')],
		[sg.Text('Complemento', size=(15, 1)), sg.InputText('Endereco.CPM')],
		[sg.Text('Cep', size=(15, 1)), sg.InputText('Endereco.CEP')],
		[sg.Button('Cadastrar'), sg.Exit('Cancelar')]
 		]

		self.__window = sg.Window('Cadastro cliente', default_element_size=(40,1)).Layout(layout)

	def open(self):
		button, values = self.__window.Read()
		self.close()
		return button, values

	def cliente_cadastrado(self):
		sg.popup("Cliente cadastrado com sucesso!") 

	def ja_tem_cliente(self):
		sg.popup("Impossivel cadastrar cliente com o mesmo cpf!")

	def close(self):
		self.__window.Close()