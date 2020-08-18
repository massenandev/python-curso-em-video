from random import randint
from time import sleep
c = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
j = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
if pc == 0:
    if j == 0:
        print('Empate.')
    elif j == 1:
        print('Você venceu.')
    elif j == 2:
        print('Eu venci.')
    else:
        print('Jogada inválida.')
elif pc == 1:
    if j == 0:
        print('Eu venci.')
    elif j == 1:
        print('Empate.')
    elif j == 2:
        print('Você venceu.')
    else:
        print('Jogada inválida.')
elif pc == 2:
    if j == 0:
        print('Você venceu.')
    elif j == 1:
        print('Eu venci.')
    elif j == 2:
        print('Empate.')
    else:
        print('Jogada inválida.')
else:
    print('')