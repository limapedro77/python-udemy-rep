def decorator(func):
    def inner(*args, **kwargs):
        for arg in args:
            is_string(arg)
        res = func(*args, **kwargs)
        return res
    return inner 

@decorator
def reverse_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parâmetros deve ser uma string')
    return reverse_string

print(reverse_string('123'))