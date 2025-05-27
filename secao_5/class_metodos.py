class Carro:
    def __init__(self, Modelo):
        self.modelo = Modelo

#Criação de método
    def acelerar(self):
        print(f'O {self.modelo} está acelerando!')

#Aplicação métodos        
fusca = Carro('Fusca')

fusca.acelerar()