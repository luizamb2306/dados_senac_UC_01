#1- Escreva um programa que, dados 2 números inteiros (n1 e n2), diga se eles são iguais ou diferentes
#2- Utilizando a estrutura do programa anterior, some os dois valores se forem diferentes e multiplique-os se forem iguais

#entrada de dados
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

#processamento dos dados
if n1 == n2:
    multiplicação = n1*n2
    #saída dos dados
    print(f'Os valores são iguais, então, o resultado é: {multiplicação:.0f}')

#processamento dos dados
else:
    soma = n1+n2
    #saída dos dados
    print(f'Os valores são diferentes, então, o resultado é: {soma:.0f}')



