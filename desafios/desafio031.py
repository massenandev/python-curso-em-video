v = int(input('Qual a distância da viagem em KM? '))
if v <= 200:
    print('Você pagará R${:.1f}.'.format(v*0.5))
else:
    print('Você pagará R${:.1f}.'.format(v*0.45))
