class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    
    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
        
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
        
c1 = Cliente('Davi')
c1.inserir_endereco('Av Brasil', 123)
c1.inserir_endereco('Rua 2', 321)
c1.listar_endereco()