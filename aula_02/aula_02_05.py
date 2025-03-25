#1- Faça um programa que leia uma temperatura em graus Celsius e apresente-a convertida em graus
#Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a
#temperatura em Celsius

#entrada de dados
c = float(input('A temperatura em graus celsius é'))

#processamento de dados
f = ((9*c) + 160)/5

#saída de dados
print(f'A temperatura em Fahrenheit é: {f}')
