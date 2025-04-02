#3- Faça um programa que verifique a quantidade de acertos de uma prova com cinco questões, sabendo
#que serão fornecidos pelo usuário as letras assinaladas em cada questão. Para isso será criado um vetor chamado
#GABARITO com as seguintes respostas: A, B, B, D, E.

gabarito = ["a","b","b","d","e"]
prova = []
acerto = 0
erro = 0
n = 1

for i in range(5):
    prova.append(input(f'Informe a alternativa da {n}a. questão: '))
    n += 1

for i in range(len(prova)):
    if prova[i].lower() == gabarito[i].lower():
       print(f'A {i+1}a. questão está correta') 
       acerto +=1
    else:
       print(f'A {i+1}a. questão está errada')
       erro +=1

print(f' Você acertou {acerto} questões')
print(f' Você errou {erro} questões')

    

