#4- Construa um programa onde serão fornecidas as duas notas de dez alunos. Calcule
#a média de cada aluno e mostre a situação de cada aluno de acordo com as seguintes
# condições:
#- Se a média for maior igual a 70 -> ATENDIDO
#- Se a média for maior igual a 30 e menor que 70 -> PARCIALMENTE ATENDIDO
#- Se a média for menor que 30 -> NÃO ATENDIDO

#quero ler as duas notas de cada aluno e calcular a média deles e mostrar a situação atual

#estrutura de repetição 
for i in range(3):
#entrada dos dados
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a nota 1: "))
    n2 = float(input("Digite a nota 2: "))
    #processamento dos dados 
    media = (n1 + n2)/2
    if media >= 70:
        situacao = "ATENDIDO"
    elif 30 >= media <= 70:
        situacao = "PARCIALMENTE ATENDIDO"
    elif media < 30:
        situacao = "NÃO ATENDIDO"
    print(f'{nome} está com a situação {situacao}. A média foi {media}')
 #a impressão precisa ficar dentro do looping pra aparecer a nota e a situação de cada aluno
 # se a impressão fosse fora do looping, só apareceria a média do ultimo aluno
