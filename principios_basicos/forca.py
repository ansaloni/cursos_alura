import random

def jogar():
    imprimi_abertura()
    palavra_secreta = escolhe_palavra_secreta()
    tentativas = len(palavra_secreta)
    letras_acertadas = inicializa_formatacao(palavra_secreta)

    print(letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0

    while not acertou and not enforcou:

        chute = input("Chute uma letra: ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    # print("Encontrei a letra {} na posição {}".format(chute, index))
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, errou. Faltam {} tentativas.".format(tentativas - erros))

        enforcou = erros == tentativas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu! A palavra era {}".format(palavra_secreta))

    print("Fim de jogo!")

def imprimi_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def escolhe_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_formatacao(palavra):
    return ["_" for letra in palavra]

if __name__ == "__main__":
    jogar()
