#1- Utilizando apenas o conceito de repetição, faça um programa para ler 2 valores e
#se o segundo valor informado for ZERO, deve ser lido um novo valor, pois o segundo valor
#não pode ser igual a zero. Ao final imprimir o resultado da divisão do primeiro valor pelo
#segundo valor

segundo_valor = 0

while segundo_valor == 0:
    
    primeiro_valor = float(input("Digite aqui o primeiro valor"))
    segundo_valor = float(input("Digite aqui o segundo valor"))
    
    if segundo_valor == 0:
        print('Informe o segundo valor novamente') 
    else:
        primeiro_valor / segundo_valor
   

