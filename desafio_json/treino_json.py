import json
from pathlib import Path

# Procurando o arquivo filmes.json
caminho = Path(__file__).parent.parent / 'filmes.json'

# Abrindo o arquivo json para manipulação
with open(caminho, 'r', encoding='utf-8') as arquivo:
    informacoes = json.load(arquivo)

# Adicionando um novo filme ao json
novo_filme = {
    "titulo": "Clube da Luta",
    "ano": 1999,
    "genero": ["Drama"],
    "nota": 8.8
}

filmes = informacoes['filmes']

filmes.append(novo_filme)

# Alterando a nota e adicionando novo gênero
for filme in filmes:
    if filme['titulo'] == 'Interestelar':
        filme['nota'] = 9.0
        
    if filme['titulo'] == 'O Poderoso Chefão':
        filme['genero'].append("Suspense")

# Criando novo caminho com o json atualizado
caminho_novo = Path(__file__).parent.parent / 'filmes_atualizados.json'

with open(caminho_novo, 'w', encoding='utf-8') as arquivo:
    informacoes = json.dump(informacoes, arquivo, indent=2, ensure_ascii=False)