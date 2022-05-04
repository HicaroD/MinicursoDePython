# Conjunto: Imutável, não indexável, não ordenada, não suportar elementos duplicados
numeros = {1, 2, 3}
numeros.add(10)
numeros.remove(2)
numeros.add(10)
numeros.add(10)
numeros.add(10)

print(numeros)

for numero in numeros:
    print(numero)

if 1 in numeros:
    print("1 está contido no conjunto")