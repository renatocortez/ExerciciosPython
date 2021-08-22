'''DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES.
 SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE-O'''

soma = 0
for c in range(1, 7):
    n = int(input(f'{c}º número: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares é igual a {soma}.')