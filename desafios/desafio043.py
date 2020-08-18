peso = float(input('Qual o seu peso em kg? '))
alt = float(input('Qual a sua altura em m? '))
imc = peso / (alt * alt)
if imc < 18.5:
    print('Seu IMC é {:.2f} e a classificação é: Abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f} e a classificação é: Peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f} e a classificação é: Sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.2f} e a classificação é: Obesidade'.format(imc))
else:
    print('Seu IMC é {:.2f} e a classificação é: Obesidade mórbida'.format(imc))
