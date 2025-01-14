from carro import Carro
from moto import Moto

class Garagem:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.veiculos = []  # Lista para armazenar veículos estacionados

    def estacionar(self, veiculo):
        if len(self.veiculos) < self.capacidade:
            self.veiculos.append(veiculo)
            print(f"Veículo {veiculo} estacionado com sucesso!")
        else:
            print("Garagem cheia! Não há espaço para mais veículos.")

    def retirar(self, placa):
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                self.veiculos.remove(veiculo)
                print(f"Veículo {veiculo} retirado com sucesso!")
                return
        print("Veículo não encontrado!")

    def listar_veiculos(self):
        if len(self.veiculos) == 0:
            print("Nenhum veículo estacionado.")
        else:
            print("Veículos estacionados:")
            for veiculo in self.veiculos:
                print(veiculo)

    def __str__(self):
        return f"Garagem com capacidade para {self.capacidade} veículos e {len(self.veiculos)} veículos estacionados."
