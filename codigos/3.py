idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Pode votar")
elif idade == 16:
    print("Tem 16 anos, mas mesmo assim não pode votar")
else:
    print("Não pode votar")