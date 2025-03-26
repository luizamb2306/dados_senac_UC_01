##1- Faça um programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu
##nas últimas 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições:
##->Ter entre 16 e 69 anos.
##-> Pesar mais de 50 kg.
##-> Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)

#entrada de dados
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))
horas_de_sono = int(input("Digite quantas horas de sono você teve nas últimas 24hrs: "))

#processamento dos dados
if idade >= 16 and idade <= 69 and peso >= 50 and horas_de_sono >=6:
    #saída dos dados
    print(f'Pode doar!')
elif idade < 16:
    #saída dos dados
    print(f'Não pode doar, porque a sua idade é menor que 16 anos')
elif peso < 50:
    #saída dos dados
    print(f'Não pode doar, porque o seu peso é menor que 50kg')
elif horas_de_sono < 6:
    #saída dos dados
    print(f'Não pode doar, porque dormiu menos que 6 horas')

# essa solução é não é a ideal porque só testa uma das condições não atendidas, sendo que pode ter mais de uma condição não atendida... Então, o ideal seria colocar um if dentro do outro e fazer um código maior que abranja todas as condições... Ou, usar uma estrutura de loop que vamos aprender mais pra frente 


