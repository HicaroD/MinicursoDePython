#Explicar o def
#Parâmetros
#Formas de retornar o valor: printando ou usando o return

def média(nota1, nota2): #com parâmetros
    média = (nota1 + nota2)/2
    print(média)

#Ou
def média_input(): #sem parâmetros
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2)/2
    print(média)

#Usando return
def média_return():
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2)/2
    return média #O return não só retorna um valor ele também interrompe o restante da função. (tipo break)
nota1 = 12
nota2 = 13
média(nota1, nota2)
print('-=-=-=-=-=-=-=-')
média_input()
print('-=-=-=-=-=-=-=-')
print(média_return())#Retornando um valor! por isso o uso do print.

#Desafios:
#Melhore os desafios 04, 05, 06 utilizando funções.