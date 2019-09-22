from abstractChamado import AbstractChamado
from tipoChamado import TipoChamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class Chamado(AbstractChamado):
    def __init__(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado):

            self.__data = data
            self.__cliente = cliente
            self.__tecnico = tecnico
            self.__titulo = titulo
            self.__descricao = descricao
            self.__prioridade = prioridade
            self.__tipo_chamado = tipo

    @property
    def data(self):
        return self.__data

    @property
    def cliente(self):
        return self.__cliente

    @property
    def tecnico(self):
        return self.__tecnico

    @property
    def titulo(self):
        return self.__descricao

    @property  
    def descricao(self):
        return self.__descricao

    @property   
    def prioridade(self):
        return self.__prioridade
    @property
    def tipo_chamado(self):
        return self.__tipo_chamado

    @data.setter
    def data(self, data: Date):
        if (isinstance(Date, data)):
            self.__data = data

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(Cliente, cliente):
            self.__cliente = cliente

    @tecnico.setter
    def tecnico(self, tec: Tecnico):
        if (isinstance(Tecnico, tec)):
            self.__tecnico = tec

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @descricao.setter  
    def descricao(self, desc: str):
        return self.__descricao

    @prioridade.setter   
    def prioridade(self, prioridade: int):
        self.__prioridade = prioridade

    @tipo_chamado.setter
    def tipo_chamado(self, chamado: Chamado):
        if (isinstance(Chamado, chamado)):
            self.__tipo_chamado = chamado