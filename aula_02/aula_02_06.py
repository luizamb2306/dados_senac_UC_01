#Escreva um programa que calcule a velocidade média de um veículo com base na distância percorrida
#e no tempo em que uma viagem foi realizada

#entrada de dados
distancia = float(input('A distância percorrida em KM foi:'))
tempo = float(input('O tempo de viagem em horas foi'))

#processamento de dados
velocidade_média = distancia / tempo

#saída de dados
print(f'A velocidade média foi de {velocidade_média:.1f} KM/Hora')

#3 – Com base nos dados obtidos no programa anterior e sabendo que o veículo usado consome 12 Km/l,
#construa um programa que determine a quantidade de combustível gasto nessa viagem

#entrada de dados - consumo por litro
taxa_de_consumo = 12

#processamento de dados
combustível = (1/taxa_de_consumo) * distancia

#saída de dados
print(f'O consumo de combustível foi de {combustível:.2f} litros.')

