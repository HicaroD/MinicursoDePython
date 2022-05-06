"""
Escreva uma função que recebe uma coleção de elementos e remova todos os elementos
repetidos

Input:
[1, 2, 3, 3]

Output:
[1, 2, 3]
"""
def remova_repetidos(lista):
    temp = []
    for elemento in lista:
        if elemento not in temp:
            temp.append(elemento)
    return temp

x = [1, 2, 2, 3, 4, 5, 6, 7, 10, 10, 11, 12, 120, 121]
# unicos = remova_repetidos(x)
unicos = set(x)
print(unicos)