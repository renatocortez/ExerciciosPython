total = 0
n = int(input('Digite um número para saber se ele é primo: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end='')
        total += 1
    else:
        print('\033[033m', end='')
    print(f'{c}', end='')
print(f'\n\033[mO número {n} é divisível {total} vezes.')
if total == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo.')
