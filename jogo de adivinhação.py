print("*******************")
print("JOGO DE ADIVINHAÇÃO")
print("*******************")

numero_secreto = 32

chute = input("Digite seu número no console:  ")

chute= int(chute)

print("Você digitou" , chute)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do jogo.")