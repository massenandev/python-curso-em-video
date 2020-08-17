from datetime import date
ano = int(input('Em que ano o atleta nasceu? '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Júnior')
elif 19 < idade <= 20:
    print('Sênior')
else:
    print('Master')
