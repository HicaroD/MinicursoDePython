'''
Exercício Python 5: Crie um programa que mostre na tela todos os números pares que estão 
no intervalo entre 1 e 50.
'''

for x in range(0, 51):
    print(x)

'''
Exercício Python 13: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual 
foi o maior e o menor peso lidos.
'''

for x in range(5):
    peso = float(input('Peso[Kg]: '))
    if x == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}kg')
print(f'O menor peso foi {menor}kg')

'''
Exercício Python 14: Desenvolva um programa que leia a idade de 4 pessoas. No final do programa 
mostre a média de idade do grupo.
'''
total = 0
for x in range(4):
    idade = float(input('Idade: '))
    total += idade

print(f'A média da idade do grupo foi de {(total/4):.0f} anos')

'''
Exercício Python 23: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''
maiores = 0
homens = 0
mulher_m20 = 0
r = 'S'
while r in 'Ss':
    idade = float(input('Idade: '))
    sexo = input('Digite seu sexo[M/F]: ')
    if idade > 18:
        maiores += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulher_m20 += 1
    r = input('Deseja continuar?[S/N]: ')

print(f'Ao todo foram {maiores} pessoas tem mais de 18 anos')
print(f'Ao todo {homens} homens foram cadastrados.')
print(f'Ao todo {mulher_m20} mulheres cadastradas tem menos de 20 anos.')

'''
Exercício Python 25: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte 
ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada 
valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e moedas de R$1.
'''
valor = int(input('Valor a ser sacado: R$'))
nota_50 = 0
nota_20 = 0
nota_10 = 0
moeda_1 = 0
while valor>=50:
    valor -= 50
    nota_50 += 1
while valor>=20:
    valor -= 20
    nota_20 += 1
while valor >= 10:
    valor -= 10
    nota_10 += 1
while valor >= 1:
    valor -= 1
    moeda_1 += 1

print(f'O valor de R${valor:.2f} foi sacado em: ')
print(f'{nota_50} notas de R$50, {nota_20} notas de R$20, {nota_10} notas de R$10, {moeda_1} moedas de R$1')