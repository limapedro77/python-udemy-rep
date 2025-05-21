import random

for _ in range(10000):
    cpf_limpo = ''

    for i in range (9):
        cpf_limpo += str(random.randint(0,9))

    multiplicador = 10
    soma1  = 0

    for numero in cpf_limpo[:9]:
        soma1 += int(numero) * multiplicador
        multiplicador -= 1

    soma1 = (soma1 * 10 ) % 11 
    if soma1 > 9:
        soma1 = 0 

    multiplicador = 11 
    soma2 = 0
    cpf_primeiro_digito = cpf_limpo[:9] + str(soma1)

    for numero in cpf_primeiro_digito:
        soma2 += int(numero) * multiplicador
        multiplicador -= 1

    soma2 = (soma2 * 10 ) % 11 
    if soma2 > 9:
        soma2 = 0

    cpf_dois_digitos = cpf_primeiro_digito + str(soma2)

    print(cpf_dois_digitos)




