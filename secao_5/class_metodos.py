class Carro:
    def __init__(self, Marca, Modelo, Ano):
        self.modelo = Modelo
        self.marca = Marca
        self.ano = Ano

#Criação de método
    def acelerar(self):
        print(f'O {self.modelo} da {self.marca} do ano {self.ano} está acelerando!')

#Aplicação métodos        
fusca = Carro('Wolkswagen','Fusca','1969')

fusca.acelerar()