#O que é uma tupla?
#Imutável!
#Indices das tuplas!
#Como percorrer uma tupla?

tupla = (10, 20)
print(tupla[0]) #Primeiro índice
print(tupla[1]) #Segundo índice
print(tupla[-1]) #Ultimo índice
#OBS: Em python o ultimo elemento pode ser pego utilizando -1 como index!

for x in tupla:
    print(x)
#OU
for l in range(0, len(tupla)-1):
    print(tupla[l])
#ERRO!!!
for x in tupla:
    tupla[x] = 12

#UNIÃO DE TUPLAS (concatenação)
tupla_a = ('a', 'b', 'c')
tupla_b = ('d', 'e', 'f')
tupla_c = tupla_a + tupla_b
print(tupla_c) #Eu posso criar outra tupla utilizando diferentes tuplas, mas n posso alterar os elemento da tupla_a
#EXEMPLO DE ERRO:
for x in range(0, 2): #Tamanho das tuplas A e B
    tupla_a[x] = tupla_b[x]
print(tupla_a)

#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

#) Quais foram os números pares.

#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.

#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, 
#para cada palavra, quais são as suas vogais.