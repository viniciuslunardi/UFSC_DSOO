class NaoTemCliente(Exception):
    def __init__(self):
        super().__init__("Nao há clientes com esse cpf!")
