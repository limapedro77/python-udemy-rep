try:

    horario = int(input("Digite o horário: "))

    if horario >= 0 and horario < 12:
        print("Bom dia!")
    if horario >= 12 and horario < 18:
        print("Boa tarde!")
    if horario >= 18 and horario < 24:
        print("Boa noite!")
    if horario >= 24:
        print("Digite um horário dentro dos limites")

except ValueError:
    print("Digite um horário válido!")

