import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")  # Texto de apresentação do game
    print("*********************************")

    numero_aleat = random.randrange(1,101)
    numero_secreto = int(numero_aleat)
    tentativa = 0                           # Variaveis utilizadas no game
    rodada = 1
    ponto = 1000

    print("Escolha o nível de Dificuldade:", numero_secreto)
    print("(1) fácil (2) Médio (3) Difícil")   #Bloco de escolha da Dificuldade
    nivel =int(input("Defina o nível:"))

    if (nivel == 1):
        tentativa = 20
    elif (nivel == 2):     # Condição se para definir a dificuldade
        tentativa = 10
    else:
        tentativa = 3
    


    for rodada in range(1,tentativa + 1):
        print("Tentativa {} de {}".format(rodada,tentativa))
        chute_str = int(input("Digite um número de 1 a 100: "))
        print("Você digitou: ", chute_str)
                                                              #Condição for para verificar os se os palpites acertam
        if(chute_str < 31 or chute_str > 100):
            print("Você deve digitar um número entre 1 e 100",)
            continue

        maior = chute_str > numero_secreto
        menor = chute_str < numero_secreto

        if (numero_secreto == chute_str):
            print("Você acertou e fez {} pontos!".format(ponto))
            break
        elif (chute_str < numero_secreto):
            print('O número escolhido é menor que o secreto.')
        elif(chute_str > numero_secreto):
            print('O número escolhido é maior que o secreto')
        else:
            print("Você errou e marcou um total{}!".format(ponto))
        pontos_perdidos = abs(numero_secreto - chute_str)
        ponto = ponto - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

