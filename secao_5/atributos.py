class Pessoa:
# possível criar variáveis da classe
    ano_atual = 2020    
    ano_atual = 2020
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        print(f'O {self.nome} nasceu em {Pessoa.ano_atual - self.idade}')
                                        #assim que chama
p1 = Pessoa('Luiz', 32)
p1.get_ano_nascimento()
