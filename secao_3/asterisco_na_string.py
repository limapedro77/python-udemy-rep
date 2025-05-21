nome = str(input('Digite seu nome completo: '))
novo_nome = ''
i = 0

while i < len(nome):
    letra = nome[i]
    i += 1
    novo_nome += f'*{letra}'
print(novo_nome + '*')