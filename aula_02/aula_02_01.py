# A Estrutura Sequencial, é um conjunto de instruções no qual cada uma delas será
#executada uma após a outra.
# Primeiramente, é feita a declaração das variáveis, posteriormente, são executados os
# comandos de entrada e/ou atribuição.
# Na sequência é realizado o processamento dos dados e, no final, realiza-se a saída
# de dados

#programa média
# Um detalhe importante a ser lembrado é que a função input() sempre lê strings. Por
# isso, caso você deseje ler um número, deverá converter o dado retornado por essa função
#para o formato numérico apropriado
# função f string -> coloca a variável dentro do texto

# entrada de dados
nome = input('Informe o nome do estudante')
n1 = float(input(f'Informe a primeira nota {nome}:'))
n2 = float(input(f'Informe a segunda nota {nome}:'))
n3 = float(input(f'Informe a terceira nota {nome}:'))

#processamento dos dados
media = (n1+n2+n3)/3

#saida dos dados

print(f'A sua média foi: {media:.1f}')
# {media:.1f} => quer dizer, quero que use uma casa decimal depois do ponto

# pra quebrar linha => ALT Z
# pra movimentar a linha => ALT Seta pra cima

