class Veiculo:
    def __init__(self, modelo, placa, tipo):
        self.modelo = modelo
        self.placa = placa
        self.tipo = tipo  # Tipo pode ser "Carro", "Moto", etc.

    def __str__(self):
        return f"{self.modelo} - {self.placa} ({self.tipo})"
