from controladores.controladorRestaurante import ControladorRestaurante
class TelaPrincipal:
    def __init__(self, controlador):
        self.__controlador_restaurante = controlador

    def opcao(self):
        pass

    def boas_vindas(self):
        print("----------------BEM VINDO AO RESTAURANTE PAPATIN-----------------")
        print("Para entrar como funcionario - Digite 1")
        print("Para entrar como cliente - Digite 2")
