def contar_letras(texto):
    texto = texto.lower()  
    letras = {}
    for caractere in texto:
        if caractere.isalpha():  
            if caractere in letras:
                letras[caractere] += 1
            else:
                letras[caractere] = 1
    return letras

frase = input("Digite uma frase: ")
resultado = contar_letras(frase)

for letra, quantidade in resultado.items():
    print(f"Letra '{letra}': {quantidade}x")

