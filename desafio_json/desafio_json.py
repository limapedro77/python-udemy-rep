import json
from pathlib import Path

caminho = Path(__file__).parent / 'filmes2.json'

with open(caminho, 'r', encoding='utf-8') as arquivo:
    informacoes = json.load(arquivo)

while True:
    print("\n---  Bem-vindo ao sistema de cadastro e busca de filmes ---")
    print("1 - Listar todos os filmes")
    print("2 - Adicionar um novo filme")
    print("3 - Buscar filme pelo título e exibir suas informações")
    print("4 - Atualizar a nota de um filme existente")
    print("5 - Remover um filme pelo título")
    print("6 - Salvar as alterações")
    print("7 - Sair do programa")
    opcao = input("Digite o número da opção desejada: ").strip()[0]
    
    if opcao == '1':
        print("\n\nLista de filmes:\n")
        for filme in informacoes['filmes']:
            print(f"Título: {filme['titulo']}")
            print(f"Ano: {filme['ano']}")
            print(f"Gênero: {filme['genero']}")
            print(f"Nota: {filme['nota']}")
            print()
    
    elif opcao == '2':
        novo_filme = {
            "titulo": input("Digite o título do filme: "),
            "ano": int(input("Digite o ano do filme: ")),
            "genero": input("Digite o gênero do filme: ").split(", "),
            "nota": float(input("Digite a nota do filme: "))
        }
        informacoes['filmes'].append(novo_filme)
        print("Filme adicionado com sucesso!")
    
    elif opcao == '3':
        titulo = input("Digite o título do filme que deseja buscar: ")
        for filme in informacoes['filmes']:
            if filme['titulo'].lower() == titulo.lower():
                print("\n\nInformações do filme:\n")
                print(f"Título: {filme['titulo']}")
                print(f"Ano: {filme['ano']}")
                print(f"Gênero: {filme['genero']}")
                print(f"Nota: {filme['nota']}")
                break
        else:
            print("Filme não encontrado.")

    elif opcao == '4':
        titulo = input("Digite o título do filme que deseja atualizar: ")
        for filme in informacoes['filmes']:
            if filme['titulo'].lower() == titulo.lower():
                filme['nota'] = float(input("Digite a nova nota do filme: "))
                print("Nota atualizada com sucesso!")
                break
    
    elif opcao == '5':
        titulo = input("Digite o título do filme que deseja remover: ")
        for filme in informacoes['filmes']:
            if filme['titulo'].lower() == titulo.lower():
                informacoes['filmes'].remove(filme)
                print("Filme removido com sucesso!")
                break
    
    elif opcao == '6':
        with open(caminho, 'w', encoding='utf-8') as arquivo:
            json.dump(informacoes, arquivo, indent=2, ensure_ascii=False)
        print("Alterações salvas com sucesso!")
    
    elif opcao == '7':
        print("Saindo do programa...")
        break