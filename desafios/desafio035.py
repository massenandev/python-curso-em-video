um = float(input('Qual a primeira reta? '))
dois = float(input('Qual a segunda reta? '))
tres = float(input('Qual a terceira reta? '))
if um < dois + tres and dois < um + tres and tres < um + dois:
    print('Pode formar um triângulo.')
else:
    print('Não pode formar um triângulo.')

