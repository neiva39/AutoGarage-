from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, placa):
        super().__init__(modelo, placa, tipo="Carro")

    def __str__(self):
        return f"Carro - {super().__str__()}"

