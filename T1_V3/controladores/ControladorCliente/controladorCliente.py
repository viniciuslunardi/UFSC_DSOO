from telas.telaCliente import TelaCliente
from entidades.endereco import Endereco
from entidades.cliente import Cliente
from excecoes.jaExisteClienteException import JaTemCliente
from controladores.ControladorCliente.cliente_db import ClienteDB
cliente_db = ClienteDB('./controladores/ControladorCliente/cliente.db')
class ControladorCliente():
    def __init__(self, controlador_principal):
        self.__clientes = []
        self.__clientes_excluido = []
        self.__cliente_atual = None
        self.__main_view = TelaCliente()
        self.__controlador_principal = controlador_principal
        self.religa_sistema()

    def religa_sistema(self):
        clientes = cliente_db.fetch()
        fidelidade = 0
        for cliente in clientes:
            velho_cliente = Cliente(cliente[0], cliente[1], cliente[2], Endereco(cliente[3], cliente[4], cliente[5]), fidelidade, cliente[6])
            self.__clientes.append(velho_cliente)

    def autenticar(self):
        botoes, dados = self.__main_view.open_login()
        if botoes == 'Entrar':
            for cliente in self.__clientes:
                if cliente.cpf == int(dados[0]) and cliente.senha == int(dados[1]):
                    self.__cliente_atual = cliente
                    self.entrou_cliente(cliente)
                elif cliente.cpf == int(dados[0]) and cliente.senha != int(dados[1]):
                    self.__main_view.show_msg('ERROR', 'Senha invalida')

    def entrou_cliente(self, cliente):
            while True:
                eventos, dados = self.__main_view.open()
                if eventos == 'Fazer novo pedido':
                    self.__controlador_principal.cria_pedido(cliente)
                elif eventos == 'Ver pedidos':
                    self.__controlador_principal.ve_pedido_cliente(cliente)
                elif eventos == 'Mudar nome':
                    self.altera_nome()
                elif eventos == 'Mudar cpf':
                    self.altera_cpf()
                elif eventos == 'Mudar senha':
                    self.altera_senha()
                elif eventos == 'Ver dados':
                    self.ve_dados()
                elif eventos == 'Sair':
                    self.sai()
                      
    def altera_senha(self):
        eventos, dados = self.__main_view.open_senha()
        for cliente in self.__clientes:
            if cliente == self.__cliente_atual and eventos == 'Alterar':
                cliente.senha = dados[0]
                cliente_db.update(cliente.cpf, cliente.nome, cliente.telefone,
                cliente.rua, cliente.numero, cliente.complemento, dados[0])
                self.__main_view.show_msg("Senha alterada com sucesso", 'Sua alteracao foi concluida')

    def altera_nome(self):
        eventos, dados = self.__main_view.open_nome()
        for cliente in self.__clientes:
            if cliente == self.__cliente_atual and eventos == 'Alterar':
                cliente.nome = dados[0]
                cliente_db.update(cliente.cpf, dados[0], cliente.telefone,
                cliente.rua, cliente.numero, cliente.complemento, cliente.senha)
                self.__main_view.show_msg("Nome alterado com sucesso", 'Sua alteracao foi concluida')
    
    def altera_cpf(self):
        eventos, dados = self.__main_view.open_cpf()
        for cliente in self.__clientes:
            if cliente == self.__cliente_atual and eventos == 'Alterar':
                cliente.cpf = dados[0]
                self.__main_view.show_msg("cpf alterado com sucesso", 'Sua alteracao foi concluida')
        
    def inclui_cliente(self):
        novo_cliente = self.run_cadastro()
        try:
            if isinstance(novo_cliente, Cliente):
                if self.existe_cliente(novo_cliente):
                    raise JaTemCliente
                else:
                    self.__clientes.append(novo_cliente)
                    cliente_db.insert(novo_cliente.cpf, novo_cliente.nome, novo_cliente.telefone,
                    novo_cliente.rua, novo_cliente.numero, novo_cliente.complemento, novo_cliente.senha)
                    self.__main_view.show_msg("Cliente cadastrado", 
                    "Cadastro efetuado com sucesso.")
        except JaTemCliente:
            return self.__main_view.show_msg("Cadastro nao efetuado",
            "Cadastro nao efetuado pois esse cpf ja esta cadastrado.")

    def exclui_cliente(self, cpf: int):
        try:
            for cliente in self.__clientes:
                if cliente.cpf == cpf:
                    self.__clientes_excluido.append(cliente)
                    cliente_db.remove(cliente.cpf)
                    self.__main_view.show_msg("Exclusao", 'Cliente excluido com sucesso.')
                    self.__clientes = list(filter(lambda i: i.cpf != cpf, self.__clientes))  
            raise Exception  
        except Exception:
            self.__main_view.show_msg("ERROR", 'Cliente nao foi localizado')

    def existe_cliente(self, c1):
        for clientes in self.__clientes:
            if clientes == c1:
                return True
        return False
                
    def ve_clientes(self):
        if self.__clientes:
            self.__main_view.show_msg('Clientes cadastrado', str(self.__clientes))
        else:
            self.__main_view.show_msg('ERROR', 'Nao existem clientes cadastrados')
    
    def ve_clientes_excluidos(self):
        if self.__clientes_excluido:
            self.__main_view.show_msg('Clientes excluidos', str({self.__clientes_excluido}))
        else: 
            self.__main_view.show_msg('ERROR', 'Nao existem clientes excluidos')

    def run_cadastro(self):
        while True:    
            botao, dados = self.__main_view.open_cadastro()
            if botao == 'Cadastrar':
                if isinstance(dados[4], int) and isinstance(dados[1], int):
                    novo_end = Endereco(dados[3], int(dados[4]), dados[5], dados[6])
                    novo_cliente = Cliente(int(dados[1]), dados[0], dados[2], novo_end)
                    return novo_cliente
            elif botao == 'Cancelar':
                break
    
    def ve_dados(self):
        self.__main_view.show_msg('Dados cliente', str(self.__cliente_atual))

    def sai(self):
        exit(0)