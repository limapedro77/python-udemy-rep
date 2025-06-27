# permite acessar ou modificar um atributo sem precisar instanciar
class Pessoa:
    contador = 0
    
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        Pessoa.contador += 1 #ao criar uma pessoa o contador aumenta 1
    
    #decora uma instancia e utiliza na função (fabrica)
    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anônimo',idade)
    
    # retorna o contador sem precisar de instancia
    @classmethod
    def ver_contador(cls):
        return cls.contador

print(Pessoa.ver_contador())
p1 = Pessoa.criar_anonimo(31)
print(p1.nome, p1.idade)  
print(Pessoa.ver_contador())
 



    