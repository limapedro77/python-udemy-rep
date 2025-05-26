import time
# def decorator(func):
#     def inner(*args, **kwargs):
#         for arg in args:
#             is_string(arg)
#         res = func(*args, **kwargs)
#         return res
#     return inner 

# @decorator
# def reverse_string(string):
#     return string[::-1]

# def is_string(param):
#     if not isinstance(param, str):
#         raise TypeError('Parâmetros deve ser uma string')
#     return reverse_string

# print(reverse_string('123'))

import time

def validate_and_time(func):
    def inner(*args, **kwargs):
        for arg in args:
            isnumber(arg)
        for value in kwargs.values():
            isnumber(value)

        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Tempo de execução de '{func.__name__}': {elapsed:.6f} segundos")
        return(f'Resultado: {result}')
    return inner 

@validate_and_time
def somar(*nums):
    return sum(nums)

def isnumber(param):
    if not isinstance(param, (int, float)):
        raise TypeError('Parâmetros devem ser do tipo int ou float')

print(somar(33, 21, 32,))
