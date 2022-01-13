import random
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")  # Texto de apresentação do game
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]



    enforcou = False
    acertou = False
    erro = 0

    print(letras_acertadas)

    #enquanto não enforcou(false) ou acertou(false):
    while (not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()  #Função que elimina o problema dos espaços digitados

        if (chute in palavra_secreta): #if para vericar se a letra esta correta
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):  #Funcao para eliminar o problema das letras maisculas.
                    letras_acertadas[index] = letra
                index += 1
        else:
            erro += 1
        enforcou = erro == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if (acertou):
        print("Parabéns você ganhou =) ")
    else:
        print("Você perdeu =( ")


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()