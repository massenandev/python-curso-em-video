#nome = input('Qual é o seu nome?')
#print('Prazer em te conhecer{:=^20}!'.format(nome))

n1 = int(input('Primeiro valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1//n2
e = n1 ** n2
#:.3f indica que o resultado virá formatado com 3 casas flutuantes
# ,end = '' impede que pule uma linha (cola as linhas) e \n quebra a linha, assim como no java
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s,m,d))
print('A divisão inteira é {} e a potência é {}'.format(di, e))
