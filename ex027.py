'''FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA
 E MOSTRE O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE.'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))



