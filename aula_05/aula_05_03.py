# adicionar funções matemáticas ao resumo

num = [10,8,3,4,5,8,78,95,15,87]
soma = sum(num)
maior = max(num)
menor = min(num)
count = len(num)
media = soma/count
num.sort(reverse=True)
index = num.index(3) ## essa função nos diz a posição de determinado item em uma lista

print(soma)
print(maior)
print(menor)
print(media)
print(num)
print(index)

