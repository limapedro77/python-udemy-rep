import random
numero_secreto = random.randint(0,10)
tentativas = 1
chute=0

while chute != numero_secreto:
    print(f'Tentativa {tentativas}')
    chute = int(input("Digite um número entre 0 e 10: "))
    if chute == numero_secreto:
        print("Você acertou!")
    else:
        continuar= str(input("Você errou, quer continuar? [S/N]")).upper().strip()[0]
        if continuar in "N":
            break
        elif continuar in "S" and chute > numero_secreto:
            print("O número secreto é menor.")
        elif chute < numero_secreto:
            print("O número secreto é maior.")
        tentativas += 1
if continuar in "N":
    print("Obrigado por jogar!")
if tentativas == 1 and continuar in "S":
    print("E você acertou de primeira!")
elif tentativas > 1 and tentativas <= 3 and continuar in "S":
    print(f"Acertou rápido em {tentativas} tentativas, parabéns!")
elif continuar in "S":
    print(f"Mas acertou em {tentativas}, pode melhorar!")
