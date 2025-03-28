#2- Faça um programa que receba do usuário o nome e a idade de 10 pessoas. Ao final
#mostre a soma e a média das idades.

#entrada de dados

soma = 0
mais_velho = 0
mais_novo = 200

for i in range(3):
    nome = input('Informe o nome do usuário: ')
    idade = int(input('Informe a idade do usuário: '))
   
    # se a idade digitada é maior do que a tenho guardada, essa é a maior idade 
    if idade > mais_velho:
        mais_velho = idade
        maior_nome = nome
    
    if idade < mais_novo:
        mais_novo = idade
        menor_nome = nome

    soma = soma + idade

print(f'A soma das idades foi {soma}')
print(f'A média das idades foi {(soma / (i+1)):.1f}')
print(f' A pessoa mais velha é: {maior_nome} e a pessoa mais nova é {menor_nome}')



