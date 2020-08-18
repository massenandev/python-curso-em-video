pro = float(input('Qual o valor do produto? '))
print('''Formas de pagamento:
[ 1 ] à vista: dinheiro ou cheque
[ 2 ] à vista, no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
meio = int(input('Qual o meio de pagamento? '))
if meio == 1:
    print('O valor fica R${}.'.format(pro -(pro*0.1)))
elif meio == 2:
    print('O valor fica R${}.'.format(pro-(pro*0.15)))
elif meio == 3:
    print('O valor fica R${}.'.format(pro))
elif meio == 4:
    print('O valor fica R${}.'.format(pro+(pro*0.2)))
else:
    print('Opção inválida.')

