# colorindo
print('\033[31mOlá, Mundo!')
print('\033[31;43mOlá, Mundo!')
print('\033[1;31mOlá, Mundo!')
print('\033[31mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[32mOlá, Mundo!\033[m')
print('\033[7;36;44mOlá, Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}'.format(a, b))

nome = 'Guanabara'
print('Olá, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))
