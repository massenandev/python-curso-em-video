n1 = int(input('Qual o primeiro número? '))
n2 = int(input('Qual o segundo número? '))
if n1 > n2:
    print('O maior valor é {} e o menor é {}.'.format(n1, n2))
elif n2 > n1:
    print('O maior valor é {} e o menor é {}.'.format(n2, n1))
else:
    print('Os valores são iguais.')
