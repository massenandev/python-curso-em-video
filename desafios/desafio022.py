nome = input('Digite seu nome completo: ').strip()
s = nome.split()
print('Maiúsculo, fica: {}'.format(nome.upper()))
print('Minúsculo, fica: {}'.format(nome.lower()))
print('Sem espaços, contém {} caracteres.'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras.'.format(len(s[0])))
