class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco
        # o ._ convenção diz para usar o atributo somente dentro da classe
        
    @property   #permite transformar um metodo em um "atributo falso" e da para o usuario chamar como um atributo print(x.y)
    def preco (self):
        return self._preco #permite a manipulação desse falso atributo com contas e etc
    
    @preco.setter #permite a alteração desse atributo falso e é possivel fazer checagem
    def preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError ("O preço não pode ser negativo")
        self._preco = novo_preco
        
c = Produto('Caneta', 5)
print(c.preco) #usuario chama um metodo como um atributo
c.preco = 10  #alteração do falso atributo
print(c.preco)
c.preco = -5  #nao permite
        