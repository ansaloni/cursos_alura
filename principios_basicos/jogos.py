import forca
import adivinhacao


def escolhe_jogo():
    jogo = int(input("Escolha seu jogo, (1)FORCA ou (2)ADIVINHAÇÃO: "))

    if jogo == 1:
        print("Jogando Forca!")
        forca.jogar()
    elif jogo == 2:
        print("Jogando Adivinhação!")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()
