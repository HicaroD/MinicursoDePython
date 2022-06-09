def status_aluno(n1, n2):
    média = (n1 + n2)/2
    print(f'Sua média foi {média}')
    print('STATUS: ', end='')
    if média < 5:
        print('REPROVADO')
    elif 6.9 >= média >= 5:
        print('RECUPERAÇÃO')
    else:
        print('APROVADO')


nota1 = float(input('Primeira nota: '))#Os nomes das variáveis não precisa ser iguais aos dos parâmetros da função!
nota2 = float(input('Segunda nota: '))
status_aluno(nota1, nota2)