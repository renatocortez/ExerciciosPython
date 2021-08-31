'''CRIE UM PROGRAMA QUE VAI GERAR CINCO
NÚMEROS ALEATÓRIOS E COLOCA EM UM TUPLA
DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS
GERADOS E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE
ESTÃO NA TUPLA'''

from random import randint
numeros = (randint(1, 10), randint(1,10), randint(1, 10),
        randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior número sorteado foi {max(numeros)}.')
print(f'O menor número sorteado foi {min(numeros)}.')

