nome = input("Digite seu nome completo: ")
try:
    idade = int(input("Digite sua idade: "))
    
    nome_invertido = nome[::-1]

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
           
    print(f'Seu nome contém {len(nome.replace(" ", ""))} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
    
except ValueError:
    print("Digite uma idade válida (número inteiro)")
