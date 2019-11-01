class JaTemCliente(Exception):
    def __init__(self):
        super().__init__("Ja existe um cliente cadastrado com esse cpf!")
