tentativas = 1
palavra_secreta = 'banana'
letras_descobertas = ['_'] * len(palavra_secreta)

while tentativas <= len(palavra_secreta) + 3:  # Dando umas chances extras
    print(f'Tentativa {tentativas}')
    print('Palavra:', ''.join(letras_descobertas))
    
    letra_usuario = input("Digite uma letra: ").lower()

    if len(letra_usuario) > 1:
        print("Digite apenas uma letra!")
        continue

    acertou = False
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra_usuario:
            letras_descobertas[i] = letra_usuario
            acertou = True

    if acertou:
        print("Acertou!")
    else:
        print("Errou!")

    if ''.join(letras_descobertas) == palavra_secreta:
        print(f"\nVocê ganhou em {tentativas} tentativas!")
        break

    tentativas += 1

else:
    print("\nVocê perdeu!")
    print(f"A palavra era: {palavra_secreta}")
