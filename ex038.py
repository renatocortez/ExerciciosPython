'''ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E
COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
1-O PRIMEIRO VALOR É MAIOR
2-O SEGUNDO VALOR É MAIOR
3 - NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS'''

n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))

if n1 > n2:
    print(f'O número {n1} é o maior.')
elif n2 > n1:
    print(f'O número {n2} é o maior.')
else:
    print('Os valores são iguais.')



