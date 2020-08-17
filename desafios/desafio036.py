valor = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos pagará a casa? '))
pres = valor / (anos * 12)
if pres > (0.3 * sal):
    print('Empréstimo negado. A prestação seria de R${:.2f}.'.format(pres))
else:
    print('Empréstimo aprovado')

