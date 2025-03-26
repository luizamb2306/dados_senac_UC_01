##2- Escreva um programa que, dados 3 números inteiros (n1, n2 e n3), diga qual deles é maior

#entrada de dados
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#processamento de dados
if n1 > n2 and n1 > n3:
    #saída dos dados
    print(f'Dos 3 números inseridos ({n1}, {n2} e {n3}), {n1} é o maior número')
elif n2 > n1 and n2 > n3:
    #saída dos dados
    print(f'Dos 3 números inseridos ({n1}, {n2} e {n3}), {n2} é o maior número')
elif n3 > n2 and n3 > n1:
    #saída dos dados
    print(f'Dos 3 números inseridos ({n1}, {n2} e {n3}), {n3} é o maior número')


