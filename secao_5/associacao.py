#permite ligar um objeto ao outro

class Escritor:
    def __init__(self, nome, ferramenta=None):
        self.escritor = nome
        self._ferramenta = ferramenta
    
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, nova_ferramenta):
        self._ferramenta = nova_ferramenta
    
class FerramentaEscrever:
    def __init__(self, nome):
        self.nome = nome
    
    def escrever(self):
        return f'{self.nome} está escrevendo'

escritor = Escritor('João')
caneta = FerramentaEscrever('Caneta Bic')
maquina = FerramentaEscrever('Máquina de escrever')

#associação de uma classe com a outra, referenciando-a
escritor.ferramenta = maquina  # falso atributo de um vira uma classe
print(escritor.ferramenta.escrever())