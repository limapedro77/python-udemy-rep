def contagem_vogais(texto=str):
    texto = texto.lower()
    vogais = 'aeiou'
    contador = {vogal: 0 for vogal in vogais}

    for letra in texto:
        if letra in contador:
            contador[letra] += 1

    return contador

texto = input('Digite um texto: ')
print(contagem_vogais(texto))
 