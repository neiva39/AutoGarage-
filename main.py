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
