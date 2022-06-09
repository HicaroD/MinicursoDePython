#Diferente das tuplas as listas não são imutáveis
#Listas pode ter listas dentro de sí mesmas
#Listas podem ser alteradas ou receberem valores para indexes(posições) específicos
lista = [0, 1, 2, 3, 4, 5, 6]
for x in lista:
    print(x)#Elemento da lista

for y, z in enumerate(lista):
    print(y)#Posição
    print(z)#Elemento daquela posição

#ALTERANDO VALORES
lista_vazia = [None, None, None, None]
for x in range(0, len(lista_vazia)):
    lista_vazia[x] = int(input(f'Valor para [{x}]: '))
print(lista_vazia)#Valores alterados

agenda = [['João', 998124567], ['Maria', 997122345]]#Exemplo de uma agenda telefonica
for x in agenda:
    print(x)#Nome e número
    print(x[0])#Apenas o nome
    print(x[1])#Apenas o número

#FUNÇÃO APPEND /////////////////// 
#Como não podemos usar for para adiciona um elemento a um index que não exista
#na lista, utilizamos a função .append()

lista_base = [1, 2, 3]
for x in range(4, 11):
    lista_base.append(x) #Dentro dos () se aplica o valor que será adicionado.
print(lista_base) #O append adiciona o elemento na ultima posição


#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o 
#menor valor digitado e as suas respectivas posições na lista.

#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

#A) Quantas pessoas foram cadastradas.  
#B) Uma listagem com as pessoas mais pesadas.  
#C) Uma listagem com as pessoas mais leves.

#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha 
#separados os valores pares e ímpares.