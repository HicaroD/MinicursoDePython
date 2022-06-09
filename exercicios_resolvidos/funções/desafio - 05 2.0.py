def aumento_salarial(salário):#OBS: Poderia ser incluso um segundo parâmetro para alternar a condicional de aumento.
    if salário > 1250.00:
        salário_final = (salário * 0.10) + salário
        print(f'Seu salário com aumento é de: R${salário_final:.2f}')
    else:
        salário_final = (salário * 0.15) + salário
        print(f'Seu salário com aumento é de: R${salário_final:.2f}')

        
salário = float(input('Salário: R$'))
aumento_salarial(salário)