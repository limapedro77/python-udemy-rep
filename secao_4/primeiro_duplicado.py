# def zipper (lista1, lista2):
#     intervalo = min(len(lista1), len(lista2))
#     return [(lista1[i], lista2[i]) for i in range(intervalo)]

# lista1 = ['Ubatuba', 'Xique-Xique', 'Aracaju']
# lista2 = ['São Paulo', 'Bahia', 'Sergipe', 'Rio de Janeiro']

# print(zipper(lista1, lista2), sep='\n')

# ou print(zip(lista1, lista2))
# print(list(zip(lista1, lista2)))

# para zip com o maior valor
# from itertools import zip_longest
# contendo o fillvalue = 'nome para substituir o none'

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [1, 2, 3, 4]

lista_soma = [x + y for x, y in zip(lista1, lista2)]

print(lista_soma, sep=' ')