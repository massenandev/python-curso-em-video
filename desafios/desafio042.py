um = float(input('Qual a primeira reta? '))
dois = float(input('Qual a segunda reta? '))
tres = float(input('Qual a terceira reta? '))
if um < dois + tres and dois < um + tres and tres < um + dois:
    print('Pode formar um triângulo.')
if um == dois == tres:
    print('Triângulo equilátero.')
elif um == dois or dois == tres or um == tres:
    print('Triângulo isósceles.')
elif um != dois and dois != tres and um != tres:
    print('Triângulo escaleno.')
else:
    print('Não pode formar um triângulo.')
