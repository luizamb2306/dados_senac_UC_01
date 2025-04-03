#5- Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a qual coletaram os seguintes dados referentes a cada habitante para serem analisados:
#- sexo (masculino e feminino)
#- cor dos olhos (azuis, verdes ou castanhos)
#- cor dos cabelos (louros, castanhos, pretos)
#- idade
#Faça um programa que determine e escreva:
#a) a maior idade dos habitantes;
#b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
#c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;

#ENTRADA DOS DADOS:
#pedi pro copilot gerar 4 listas com 15 itens dessas 4 variáveis:
sexo = ['feminino', 'feminino', 'masculino', 'masculino', 'masculino', 'masculino', 'feminino', 'feminino', 'masculino', 'masculino', 'feminino', 'feminino', 'feminino', 'masculino', 'feminino']

cor_dos_olhos = ['castanhos', 'verdes', 'castanhos', 'castanhos', 'castanhos', 'castanhos', 'castanhos', 'castanhos', 'verdes', 'castanhos', 'verdes', 'azuis', 'verdes', 'verdes', 'castanhos']

cor_dos_cabelos = ['pretos', 'louros', 'pretos', 'pretos', 'pretos', 'pretos', 'castanhos', 'louros', 'pretos', 'louros', 'pretos', 'louros', 'castanhos', 'louros', 'pretos']

idade = [19, 23, 32, 35, 60, 6, 56, 59, 60, 25, 7, 49, 86, 34, 92]

#PROCESSAMENTO DOS DADOS:
#identificar maior idade:

maior_idade = 0

for i in range(len(idade)):
    if idade[i] >  maior_idade:
        maior_idade = idade[i]

#criar lista de individuos sexo femino idade entre 18 e 35 inclusive e contar 
lista_FEM_18_35 = []

for i in range(len(idade)):
    if idade[i] >= 18 and idade[i] <= 35 and sexo[i] == 'feminino':
       lista_FEM_18_35.append(idade[i]) 

qtd_fem_18_35 = len(lista_FEM_18_35)

#criar lista de individuos com olhos verdes e cabelos loiros e contar

lista_verde_loiro = []

for i in range(len(idade)):
    if cor_dos_olhos[i] == 'verdes' and cor_dos_cabelos[i] == 'louros':
        lista_verde_loiro.append(idade[i])

qtd_verde_loiro = len(lista_verde_loiro)

#SAIDA DOS DADOS
print(f'A maior idade é {maior_idade}')
print(f'Quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos: {qtd_fem_18_35}')
print(f'quantidade de indivíduos que tenham olhos verdes e cabelos louros: {qtd_verde_loiro}')
