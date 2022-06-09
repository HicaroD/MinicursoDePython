for x in range(0, 5): #Repetição
    print(x)

lista = [1, 2, 3, 4, 5]
for x in lista:
    print(x)

#O for é utilizado quando se sabe quantas vezes algo vai precisar ser repetido, 
#ou se quiser percorrer uma lista/tupla/dicionário.

x = 1
y = 0
#O while se repete seguindo uma condição, até aquela condição se manter ele vai continuar se repetindo
while x > y: #Condição --> x > y
    print('X-TUDO') #Vai printar infinitamente!

#Quando não sabemos quantas vezes o programa precisará se repetir até que
#o objetivo seja alcançado, usamos o while ao invés do for.
while True: #Repetição infinita
    print(x)
    break #O break para a repetição e sai do laço
print('Fora do laço')

#Exemplo:
#Implemente um programa que pergunte valores ao usuário ate que ele digite 999 e os adicione a uma lista.
lista_valores = []
num = 0
while num != 999:
    num = int(input('Valor: '))
    lista_valores.append(num)
print(lista_valores)
#Ou
while True:
    num = int(input('Valor: '))
    if num == 999:
        break
    lista_valores.append(num)
print(lista_valores)