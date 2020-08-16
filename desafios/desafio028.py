import random
list = [0, 1, 2, 3, 4, 5]
r = random.choice(list)
num = int(input('Escolha um número entre 0 e 5: '))
if num == r:
    print('Você venceu! Eu também pensei no número {}.'.format(r))
else:
    print('Você perdeu. Eu pensei no número {}.'.format(r))

# Outra forma de responder:

'''from random import randint
computador = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ))
if jogador == computador:
    print('Você venceu!')
else:
    print('Ganhei! Eu pensei no numero {} e não no número {}.'.format(computador, jogador))'''