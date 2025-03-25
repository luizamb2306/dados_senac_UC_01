# Escreva um programa que efetue o cálculo do valor de uma prestação em atraso, utilizando
#a fórmula: valorfinal = prestacao+(prestacao*(taxa/100)*tempo)

#entrada de dados
prestacao = float(input('Informe o valor da prestação'))
taxa = float(input('Informe o valor da taxa de juros'))
tempo = int(input('Informe os dias'))

# processamento dos dados
juros = prestacao*(taxa/100)*tempo
valorfinal = prestacao+juros

#saída dos dados
print(f'A prestação encontra-se atrasada {tempo} dias e, com isso, os juros da prestação são R${juros:,.2f}, portanto, o valor final a ser pago será R${valorfinal:,.2f}')

#,.0f => a virgula antes do ponto indica que vai separar a casa de milhar


