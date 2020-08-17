from datetime import date
ano = int(input('Qual o ano em que você nasceu? '))
atual = date.today().year
a = atual - ano
if a == 18:
    print('É hora de se alistar. Você já tem {} anos.'.format(a))
elif a > 18:
    print('Já passaram {} anos do tempo de se alistar.'.format(a - 18))
else:
    print('Ainda faltam {} anos para se alistar.'.format(18 - a))