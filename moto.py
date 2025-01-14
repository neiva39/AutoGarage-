from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, placa):
        super().__init__(modelo, placa, tipo="Moto")

    def __str__(self):
        return f"Moto - {super().__str__()}"

