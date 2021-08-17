'''LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E O MENOR.'''

n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n1:
    maior = n3
print(f'O maior número é {maior} e o menor número {menor}.')


