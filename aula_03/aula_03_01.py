## estruturas de controle são para tomar decisões mediante a dados que serão processados
## o script executa uma decisão proposta por uma expressão lógica, de acordo com o resultado dessa expressão

#no if, elif e else, tem que sempre colocar : no final da condicional
# os dois pontos (:) seria o então. Se XXX, então...

# podemos usar and e or para E e OU nas expressões lógicas também

#entrada de dados:
idade=int(input('Digite sua idade: '))

#processamento e saída de dados:
if idade < 18:
    print('Você é menor de idade!')
elif idade == 18:
    print('Você tem 18 anos, acesso liberado!')
elif idade >= 65:
    print('Você tem mais de 65 anos, acesso liberado')
elif idade > 18 and idade < 65:
    print('Você tem entre 19 e 64 anos, acesso liberado')
else:
    print('Acesso liberado!')