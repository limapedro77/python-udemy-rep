# multiplicacao = 1

# def multiplica (*args):
#     global multiplicacao
#     multiplicacao = 1
#     for i in args:
#         multiplicacao *= i
#     return multiplicacao

# multiplica1 = 1,2,3,4,5,6,7,8,9,10

# print(multiplica(*multiplica1))

numero = int(input("Digite um número: "))

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(numero))