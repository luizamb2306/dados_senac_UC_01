#2- Faça um programa para uma loja de tintas, que solicite o tamanho em metros quadrados da
#área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
#a tinta é vendida em latas de 18 litros, que custam R$ 130,00.
#Informe ao usuário a quantidade de latas de tinta a serem compradas e o valor a ser pago.

#entrada de dados
area = float(input("Digite aqui a área a ser pintada em m²: "))

#processamento dos dados

#quantos litros serão necessários?
litros_tinta = area * 1/3

#quantas latas serão necessárias? 
# arredondar para cima
if (litros_tinta/18) - int(litros_tinta/18) == 0:
    latas = litros_tinta/18
else:
    latas = int(litros_tinta/18) + 1

#valor a ser pago:
valor_pg = latas*130

#saida de dados
print(f'Será necessário comprar {latas} e o valor a ser pago é R${valor_pg:.2f}')