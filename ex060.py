'''FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL'''

n = int(input('Digite um número para saber o seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}!', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
