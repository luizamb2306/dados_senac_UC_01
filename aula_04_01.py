#1- Escreva um programa que, dado 5 números inteiros, calcule a soma deles e
#identifique o maior deles.

# entrada dos dados 

soma = 0
maior = 0

# para cada variável, repetir o looping 5 vezes

for i in range(5):
    # para cada valor inteiro inputado, verificar se esse valor é maior do que a variável "maior"
    # essa variável "maior" começa no zero
    # se n for maior que 0, a variavel "maior" assume seu valor
    n = int(input('Informe um Valor Inteiro: '))
    if n>maior:
        maior = n
    soma = soma + n
        
#saída de dados
print(f'A soma é {soma:.0f} e o maior é {maior}')
