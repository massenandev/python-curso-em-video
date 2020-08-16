import random
list = [0, 1, 2, 3, 4, 5]
r = random.choice(list)
num = int(input('Escolha um número entre 0 e 5: '))
if num == r:
    print('Você venceu!')
else:
    print('Você perdeu.')
