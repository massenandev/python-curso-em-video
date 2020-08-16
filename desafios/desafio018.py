import math

a = float(input('Digite o ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O ângulo de {} tem o seno de {:.2f}'.format(a, s))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(a, c))
print('O ângulo de {} tem o tangente de {:.2f}'.format(a, t))
