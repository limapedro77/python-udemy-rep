import random

while True:
    num_computador = random.randint(1, 10)

    try:
        opcao_usuario = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        num_usuario = int(input('Digite um número (de 1 a 10): '))
        
        if opcao_usuario not in 'PI':
            raise ValueError('Digite P para Par ou I para Ímpar.')
        if num_usuario < 1 or num_usuario > 10:
            raise ValueError('Digite um número entre 1 e 10.')
        if opcao_usuario == 'I' and num_usuario % 2 == 0:
            raise ValueError('Você escolheu ÍMPAR, mas digitou um número PAR. Tente novamente.')
        if opcao_usuario == 'P' and num_usuario % 2 != 0:
            raise ValueError('Você escolheu PAR, mas digitou um número ÍMPAR. Tente novamente.')
        
    except ValueError as erro:
        print(f"Erro: {erro}")
        continue
    
    soma_opcoes = num_computador + num_usuario

    resultado = 'P' if soma_opcoes % 2 == 0 else 'I'
    resultado_texto = {'P': 'PAR', 'I': 'ÍMPAR'}[resultado]

    if resultado == opcao_usuario:
        print(f'Você ganhou! O computador escolheu {num_computador} e você {num_usuario}, somando {soma_opcoes}, que deu {resultado_texto}.')
        print('Jogue novamente!\n')
    else:
        print(f'Você perdeu! O computador escolheu {num_computador} e você {num_usuario}, somando {soma_opcoes}, que deu {resultado_texto}.')
        print('Fim de jogo.')
        break
