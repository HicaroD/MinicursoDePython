"""
Verifique se dois conjuntos têm, pelo menos, um elemento em comum.
"""

c1 = {1, 2, 3, 4, 5}
c2 = {4, 5, 6, 7}

for elemento1 in c1:
    for elemento2 in c2:
        if elemento1 == elemento2:
            print(str(elemento1) + " está contido em ambos conjuntos")

for elemento1 in c1:
    if elemento1 in c2:
        print(str(elemento1) + " está contido em ambos conjuntos")

if len(c1.intersection(c2)) > 0:
    print("Temos elementos em comum")