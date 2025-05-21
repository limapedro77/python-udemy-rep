lista_usuario = []

while True: 
    print('\nSelecione uma opção:')
    opcao = input('[i]nserir, [a]pagar, [l]istar: ').lower()[0]
    
    if opcao not in 'ial':
        print('Opção inválida')
        continue

    if opcao == 'i':
        item = input('Digite o item: ')
        lista_usuario.append(item)
        print(f'Item "{item}" inserido com sucesso.')

    elif opcao == 'a':
        if len(lista_usuario) == 0:
            print('Lista vazia. Nada a apagar.')
            continue

        try:
            indice = int(input('Digite o índice do item a ser apagado: '))
            if 0 <= indice < len(lista_usuario):
                item_a_remover = lista_usuario.pop(indice)
                print(f'Item "{item_a_remover}" apagado com sucesso.')
            else:
                print('Índice fora do alcance da lista.')
        except ValueError:
            print('Por favor, digite um número inteiro válido.')

    elif opcao == 'l':
        if len(lista_usuario) == 0:
            print('Lista vazia.')
        else:
            print('\nLista de itens:')
            for indice, item in enumerate(lista_usuario):
                print(f'{indice}: {item}')