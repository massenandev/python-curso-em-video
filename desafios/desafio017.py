from math import sqrt

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
r = ((co **2) + (ca ** 2))
print('A hipotenusa será {:.2f}'.format(sqrt(r)))

# ou então, poderiamos resolver da seguinte forma:
'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipostenusa vai medir {:.2f}'.format(hi))
'''



