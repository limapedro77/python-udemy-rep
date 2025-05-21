from itertools import product, combinations, permutations

camisas = [
    ['Preta', 'Branca'],
    ['P', 'M', 'G'],
]

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
    
print_iter(product(*camisas))