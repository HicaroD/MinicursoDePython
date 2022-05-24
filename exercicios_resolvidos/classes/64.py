"""
Escreva uma classe que represente um triângulo. Esta classe deve possuir um método 
construtor que receba os 3 lados da figura desejada. Além disso deve conter os seguintes 
comportamentos:

    a /\ c
     /__\
      b

    a) ObterPerimetro – Retorna o perímetro da figura representada
       Perímetro: Soma de todos os lados

    b) ObterTipo – Retorna o tipo do triângulo: Equilátero, Isósceles ou Escaleno

       Equilátero: Todos os lados iguais
       Isósceles: 2 lados iguais
       Escaleno:  Todos os lados diferentes
"""

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ObterPerimetro(self):
        return self.a + self.b + self.c
    
    def ObterTipo(self):
        if self.a == self.b == self.c:
            print('Equilátero')
        elif (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
            print('Isósceles')
        else:
            print('Escaleno')


a = int(input("Qual o valor do lado a?"))
b = int(input("Qual o valor do lado b?"))
c = int(input("Qual o valor do lado c?"))

t = Triangulo(a, b, c)
print(t.ObterPerimetro())
t.ObterTipo()