def radar(vel, limite):
    if vel > limite:
        multa = (vel - limite) * 7
        print('Você foi multado por está acima do limite de 80km/h')
        print(f'Valor a ser pago: R${multa:.2f}')
    else:
        print('Você está dentro dos parâmetros da lei, tenha um bom dia!')


#Com a adição da função fica bem mais fácil alterar valores, e definir novas condições.
vel = float(input('Velocidade[Km/h]: '))
radar(vel, 80) #Limite de 80km/h
radar(vel, 70) #Limite de 70km/h
radar(vel, 60) #Limite de 60km/h