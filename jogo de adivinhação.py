import random

pontos = 1000

print("JOGO DA ADIVINHAÇÃO")

numero_secreto = random.randrange(1, 101)
tentativas = 3
rodadas = 1

print("Qual nível de dificuldade?")
print("(1) Fácil")
print("(2) Médio")
print("(3) Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    tentativas = 20
elif(nivel == 2):
    tentativas = 10
else:
    tentativas = 5


for rodadas in range(1, tentativas + 1):
    print("Tentativas {} de {}".format(rodadas, tentativas))
    chute_str = input("Chute um número de 1 a 100: ")
    print("Você chutou o número", chute_str)
    chute = int(chute_str)

    maior = chute > numero_secreto
    menor = chute < numero_secreto
    acerto = chute == numero_secreto

    if (chute > 100 or chute < 1):
        print("Deve ser um número de 1 a 100!!")
        continue
    else:
        if (acerto):
            print("Você acertou e fez {} pontos)".format(pontos))
            break
        else:
            if (maior):
                print("Você chutou um número maior que o número secreto.")
            elif (menor):
                print("Você chutou um número menor que o número secreto.")

        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos

print("Você perdeu :(, O número certo é {} e sua pontuação foi {}".format(numero_secreto, pontos))
