s = float(input('Qual o valor do seu salário? '))
if s > 1250:
    print('Seu novo salário será R${:.2f}.'.format(s+(s*0.1)))
else:
    print('Seu novo salário será R${:.2f}.'.format(s+(s*0.15)))
