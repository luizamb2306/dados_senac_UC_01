#Tendo como dado de entrada à altura (h) de uma pessoa, construa um programa que calcule
#seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

# entrada de dados => processamento de dados => saída de dados

# entrada de dados
altura = float(input('Informe a sua altura em metros'))

# processamento dos dados
h = (72.7*altura) - 58
m = (62.1*altura) - 44.7

# saída dos dados
print(f'O peso ideal para homens é {h:.1f} Kg.' )
print(f'O peso ideal para mulheres é {m:.1f} Kg.' )




