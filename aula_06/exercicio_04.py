#4- Crie um programa que:
#1- Peça ao usuário para digitar dez números inteiros e os armazene em uma lista.
#2- Exiba a lista completa.
#3- Exiba o maior e o menor número da lista.
#4- Exiba a soma e a média de todos os números.

#entrada de dados
numeros = []

for i in range(10):
    numeros.append(int(input('Digite aqui os números inteiros: ')))

maior_num = 0
menor_num = 1000000000000000000000000000000

for i in range(len(numeros)):
    if numeros[i] > maior_num:
        maior_num = numeros[i]
    
    if numeros[i] < menor_num:
        menor_num = numeros[i]

soma = sum(numeros)
contagem = len(numeros)
media = soma/contagem

print(f'A lista é: {numeros}')
print(f'A média é {media} e a soma é {soma}')
