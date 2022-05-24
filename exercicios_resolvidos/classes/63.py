"""
Escreva uma classe que represente um país. Um país tem como atributos o seu nome, o nome 
da capital, sua dimensão em Km2 e sua população. A classe deve possuir os seguintes 
construtores e métodos: 

    a) Construtor que inicialize o nome, capital, dimensão e população do país; 

    b) Obter densidade demografica - Método que retorna a densidade populacional
       calculada através das propriedades do país.
"""

class Pais:
    def __init__(self, nome, nome_da_capital, dimensao, populacao):
        self.nome = nome
        self.nome_da_capital = nome_da_capital
        self.dimensao = dimensao
        self.populacao = populacao

    def densidade_demografica(self):
        return self.populacao / self.dimensao

brasil = Pais("Brasil", "Brasilia", 8514876, 213000000)
print(brasil.densidade_demografica())