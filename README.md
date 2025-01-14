Projeto Garagem

Este é um projeto simples de simulação de garagem em Python. O sistema permite o gerenciamento de veículos, incluindo carros e motos, em uma garagem com capacidade limitada. É possível estacionar, retirar e listar os veículos estacionados.

Estrutura do Projeto
O projeto é composto pelos seguintes arquivos:

veiculo.py: Contém a classe base Veiculo, que define os atributos e métodos comuns a todos os veículos.
carro.py: Contém a classe Carro, que herda de Veiculo e define comportamentos específicos para carros.
moto.py: Contém a classe Moto, que herda de Veiculo e define comportamentos específicos para motos.
garagem.py: Contém a classe Garagem, que gerencia os veículos estacionados, permitindo estacionar, retirar e listar os veículos.
main.py: Arquivo principal onde a simulação é realizada, com a criação da garagem e dos veículos, além das interações com o sistema.
Como Usar
Clone ou baixe o projeto para o seu computador.
Certifique-se de que você tem o Python instalado em sua máquina (versão 3.x recomendada).
Execute o arquivo main.py para rodar a simulação.
Exemplo de Execução
O arquivo main.py cria uma garagem, adiciona alguns veículos, tenta adicionar um veículo quando a garagem está cheia, e então realiza a remoção e listagem de veículos. O código também exibe o estado atual da garagem.

Estrutura de Código
1. Classe Veiculo (veiculo.py):
python
Copiar código
class Veiculo:
    def __init__(self, modelo, placa, tipo):
        self.modelo = modelo
        self.placa = placa
        self.tipo = tipo  # Tipo pode ser "Carro", "Moto", etc.

    def __str__(self):
        return f"{self.modelo} - {self.placa} ({self.tipo})"
2. Classe Carro (carro.py):
python
Copiar código
from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, placa):
        super().__init__(modelo, placa, tipo="Carro")

    def __str__(self):
        return f"Carro - {super().__str__()}"
3. Classe Moto (moto.py):
python
Copiar código
from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, modelo, placa):
        super().__init__(modelo, placa, tipo="Moto")

    def __str__(self):
        return f"Moto - {super().__str__()}"
4. Classe Garagem (garagem.py):
python
Copiar código
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
5. Arquivo Principal (main.py):
python
Copiar código
from garagem import Garagem
from carro import Carro
from moto import Moto

def main():
    # Criando uma garagem com capacidade para 3 veículos
    garagem = Garagem(capacidade=3)

    # Criando alguns veículos
    carro1 = Carro("Fusca", "ABC-1234")
    carro2 = Carro("Civic", "XYZ-5678")
    moto1 = Moto("XRE 300", "MNO-9876")
    moto2 = Moto("CB 500", "JKL-1234")

    # Estacionando veículos
    garagem.estacionar(carro1)
    garagem.estacionar(carro2)
    garagem.estacionar(moto1)

    # Tentando estacionar um veículo quando a garagem está cheia
    garagem.estacionar(moto2)

    # Listando veículos estacionados
    garagem.listar_veiculos()

    # Retirando um veículo
    garagem.retirar("XYZ-5678")

    # Listando veículos novamente após a retirada
    garagem.listar_veiculos()

    # Exibindo o estado da garagem
    print(garagem)

if __name__ == "__main__":
    main()
Como Rodar o Código
Clone o repositório ou faça o download dos arquivos.

No terminal, navegue até a pasta do projeto.

Execute o comando:

bash
Copiar código
python main.py
Contribuindo
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos. Para contribuir, basta fazer um fork deste repositório e enviar um pull request.

Licença
Este projeto está sob a licença MIT.


Este README.md descreve o seu projeto, fornece uma visão geral de como funciona, como rodar o código, e permite que outros desenvolvedores contribuam se desejarem.



