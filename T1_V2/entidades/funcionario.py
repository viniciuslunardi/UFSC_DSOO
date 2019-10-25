from entidades.pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, matricula: int):
        super().__init__(nome, cpf, telefone)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def telefone(self):
        return self.__telefone
    
    @matricula.setter
    def matricula(self, matricula: int):
        self.__matricula = matricula
        return print("Matricula {} adicionado com sucesso ao funcionario {}".format(self.__matricula, super().nome))

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf
    
    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone