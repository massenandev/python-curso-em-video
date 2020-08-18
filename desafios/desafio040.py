n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
m = (n1 + n2) / 2
if m <= 5:
    print('Aluno reprovado com média {:.1f}'.format(m))
elif 5 < m <= 6.9:
    print('Aluno em recuperação com média {:.1f}'.format(m))
else:
    print('Aluno aprovado com média {:.1f}'.format(m))
