#3- O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que
#leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem
#como a média delas.

#entrada de dados:

temp= []
while True: #looping infinito
   entrada = (input("Digite aqui a temperatura e, para finalizar, digite ok: "))
   if entrada == "ok":
      break
   entrada_int = int(entrada)
   temp.append(entrada_int)

#processamento de dados:
maior_temp = 0
menor_temp = 1000000000

for i in range(len(temp)):
    if temp[i] > maior_temp:
       maior_temp = temp[i]
    
    if temp[i] < menor_temp:
       menor_temp = temp[i]

soma = sum(temp)
contagem = len(temp)
media = soma/contagem

#saída de dados
print(f'A maior temperatura é {maior_temp:.1f}c e a menor temperatura é {menor_temp:.1f}c. Além disso, a média das temperaturas é {media:.1f}c')
