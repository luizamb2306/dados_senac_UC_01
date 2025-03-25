#Tendo como dado de entrada à altura (h) de uma pessoa, construa um programa que calcule
#seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

# entrada de dados => processamento de dados => saída de dados

# entrada de dados
nome = input('Informe seu nome')
h = float(input('Informe a sua altura em metros: '))
s = input('H ou M: ')


# processamento dos dados e saída dos dados

if s == "H" or s =="h":
    peso_homens = (72.7*h) - 58
    print(f'{nome}, o seu peso ideal é {peso_homens:.1f} Kg.' )

elif s == "M" or s =="m":
    peso_mulheres =(62.1*h) - 44.7
    print(f'{nome}, o seu peso ideal é {peso_mulheres:.1f} Kg.' )

else:
    print("Tente novamente" )



