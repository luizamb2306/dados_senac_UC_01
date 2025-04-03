#1- Faça um programa que pergunte quanto um funcionário recebe por hora e o número de
#horas trabalhadas no mês. Calcule e mostre o total do seu salário, sabendo que são descontados 11%
#para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a) salário bruto.
#b) Quanto pagou ao IRRF.
#c) quanto pagou ao INSS.
#d) quanto pagou ao sindicato.
#e) o salário líquido.

#entrada de dados
salario_bruto_hora = float(input('Digite aqui o seu salário bruto por hora: '))
horas_trabalhadas = float(input('Digite aqui as horas trabalhadas no mês: '))

#processamento de dados
salario_bruto = salario_bruto_hora*horas_trabalhadas

IRRF = 0.11*salario_bruto
INSS = 0.08*salario_bruto
sind = 0.05*salario_bruto

salario_liquido = salario_bruto - INSS - IRRF - sind

#saída de dados
print(f'Salário bruto de R${salario_bruto:.2f} e salário líquido de R${salario_liquido:.2f}, com um desconto total de R${(IRRF+INSS+sind):.2f}, sendo R${(IRRF):.2f} vindo de imposto de renda R${(INSS):.2f} de INSS e R${(sind):.2f} de contribuição ao sindicato')
