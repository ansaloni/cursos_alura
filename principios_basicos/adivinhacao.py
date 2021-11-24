import random


def jogar():

    print('Bem vindo ao jogo de adivinhação')

    pontos = 1000
    numero_secreto = random.randrange(1, 101)

    print("Níveis: (1)FÁCIL (2)MÉDIO  (3)DIFÍCIL")
    nivel = int(input("Escolha um nível para jogar: "))

    if nivel == 1:
        tentativas = 10
    elif nivel == 2:
        tentativas = 7
    elif nivel == 3:
        tentativas = 5

    for rodada in range(1, tentativas+1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = int(input('Dê seu palpite entre 1 e 100: '))
        print('Você chutou: ', chute)

        if chute < 1 or chute > 100:
            print("Você deve chutar um número entre 1 e 100.")
            pontos = pontos - 100
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou!")
            print("Pontuação: {}".format(pontos))
            break
        else:
            if maior:
                print("Errou! O seu chute foi maior que o número secreto.")
            elif menor:
                print("Errou! O seu chute foi menor que o número secreto.")
            pontos = pontos - abs(numero_secreto - chute)

    print("Fim de jogo!")


if __name__ == "__main__":
    jogar()
