from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self, chamados: [Chamado]):
        self.__chamados = chamados
    
    def incluiChamados(self, chamado: Chamado):
        if isinstance(Chamado, chamado):
            self.__chamados.append(chamado)
            return chamado

    def incluiTipoChamado(self, tipo: TipoChamado) -> TipoChamado:
        pass