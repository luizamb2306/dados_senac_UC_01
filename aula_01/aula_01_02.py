#1- Faça um programa que obtenha o valor para a variável HT (horas trabalhadas no mês), obtenha o valor
#para a variável VH (valor hora trabalhada), obtenha o valor para a variável PD (percentual de desconto) 
#e calcule o salário bruto => SB = HT * VH, mais o total de desconto => TD = (PD/100)*SB e o salário líquido => SL = SB – TD. 
#Apresentando ao final o Salário Liquido

#entrada de dados
taxa_PD = float(input('A taxa de desconto é:'))
horas_trabalhadas = float(input('A quantidade de horas trabalhadas no mês foi:'))
valor_hora = float(input('O valor da hora trabalhada é:'))

#processamento dos dados 
salario_bruto = horas_trabalhadas * valor_hora
desconto_total = (taxa_PD/100)*salario_bruto
salario_liquido = salario_bruto - desconto_total

#saída de dados
print(f'O salário líquido é R${salario_liquido:,.2F}')

