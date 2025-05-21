try:
    pergunta_1 = {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {
            'a': '4',
            'b': '5',
            'c': '6',
            'd': '7',
        },
        'resposta_certa': 'a',
    }

    print (pergunta_1['pergunta'])

    for chave, valor in pergunta_1['respostas'].items():
        print(f'{chave}) {valor}')


    resposta_usuario = input(str('Digite a letra da resposta: ')).strip().lower()[0]

    if resposta_usuario == pergunta_1['resposta_certa']:
        print('\nParabéns, você acertou! 👍\n')
    else:
        print('Você errou! 😢')

    pergunta_2 = {
        'pergunta2': 'Quanto é 4 x 3?',
        'respostas2': {
            'a': '10',
            'b': '12',
            'c': '14',
            'd': '16',
        },
        'resposta_certa2': 'b',
    }

    print (pergunta_2['pergunta2'])

    for chave, valor in pergunta_2['respostas2'].items():
        print(f'{chave}) {valor}')


    resposta_usuario2 = input(str('Digite a letra da resposta: ')).lower().strip()[0]

    if resposta_usuario2 == pergunta_2['resposta_certa2']:
        print('\nParabéns, você acertou! 👍\n')
    else:
        print('Você errou! 😢')

    nota = 0 
    if resposta_usuario == pergunta_1['resposta_certa']:
        nota += 5
    if resposta_usuario2 == pergunta_2['resposta_certa2']:
        nota += 5
    print(f'Sua nota foi {nota}')

except:
    print('Digite uma opção válda')