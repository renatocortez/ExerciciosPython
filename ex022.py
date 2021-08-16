'''CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
1-O NOME COM TODAS AS LETRAS MAIÚSCULAS
2-O NOME COM TODAS MINÚSCULAS
3-QUANTAS LETRAS AO TODO(SEM CONSIDERAR OS ESPAÇOS)
4 - QUANTAS LETRAS TEM O PRIMEIRO NOME'''

nome = str(input('Digite seu nome completo: '))
print('Seu nome em letras maiúsculas é:{}'.format(nome.upper()))
print('Seu nome em letras minúsculas é:{}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))

