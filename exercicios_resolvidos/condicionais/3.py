"""
Exercício Python 43: Leia um número fornecido pelo usuário. Se esse número for positivo, 
calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que
o número é inválido.
"""
numero = int(input("Qual o número que você quer? "))

if numero >= 0:
    raiz_quadrada = numero ** (0.5)
    print(raiz_quadrada)
else:
    print("Número é invalido, pois é negativo")
