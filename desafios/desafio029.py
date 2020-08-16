# a cada km acima de 80, a multa é de 7 reais
vel = int(input('Qual a velocidade? '))
if vel > 80:
    print('Você foi multado em R${}.'.format((vel-80)*7))
else:
    print('Tudo certo.')