class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(self.nome + " está falando")

p = Pessoa("Clara", 10)
print(p.nome)
print(p.idade)
p.falar()