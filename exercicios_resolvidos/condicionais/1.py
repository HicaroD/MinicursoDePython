"""
Exercício Python 41: Escreva um programa que leia do teclado as duas notas de um aluno, 
calcule e exiba a média aritmética das notas. O programa deve, adicionalmente, exibir uma 
mensagem de parabéns caso o aluno esteja aprovado (média superior ou igual a 5,0)
"""
nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))
media = (nota1 + nota2) / 2

if media >= 5.0:
    print("Parabéns, você foi aprovado")