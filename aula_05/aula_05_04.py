#2- Construa um programa que armazene 10 números inteiros em um vetor. Ao final informe quantos
#números são pares e quantos são ímpares e mostre o vetor principal na ordem inversa e depois na ordem
#crescente.

#entrada de dados
lista = []

for i in range(5):
    lista.append(int(input("Digite um número inteiro: ")))

#identificar se o numero é par ou impar
par = []
impar = []
for i in lista:
    if i%2 == 0:
        numero = "Par"
        par.append(i)
    else:
        numero = "ímpar"
        impar.append(i)

print(f'Números pares: {par}. O total é {len(par)}.')
print(f'Números ímpares: {impar}. O total é {len(impar)}.')

lista.reverse
print(f'Lista na ordem reversa: {lista}')

lista.sort()
print(f'Lista na ordem crescente: {lista}')


