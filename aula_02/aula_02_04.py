#Crie um programa que calcule a idade de uma pessoa a partir do ano de nascimento dela

#importar uma biblioteca que vai permitir trabalhar com datas
import datetime

# entrada dos dados 
data_atual = datetime.date.today()
ano_nasc = int(input('Informe o ano de nascimento:'))
ano_atual = data_atual.year

#processamento dos dados 
idade = ano_atual - ano_nasc

#saída dos dados
print(f'A idade é {idade}')

#datetime.date.today()
#datetime -> biblioteca
#date -> especifica que quer a data simples
#today -> função
#data_atual.year -> especifica que só queremos o ano da data 


