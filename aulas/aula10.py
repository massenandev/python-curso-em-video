tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

# mais imples de escrever, mas complicado de ler. Python não tem operador ternário
tempo = int(input('Quantos anos tem o seu carro? '))
print('Carro novo' if tempo <= 3 else 'Carro velho')

# os blocos sao representados por indentação/tabulação
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Parabens, vc passou.')
else:
    print('Você está em recuperação')