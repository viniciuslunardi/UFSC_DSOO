class NaoTemPedido(Exception):
    def __init__(self):
        super().__init__("Nao há pedidos!")
