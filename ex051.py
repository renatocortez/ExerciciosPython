'''DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZAO E NO FINAL,
MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.'''

primeiro = int(input('1º termo: '))
razao = int(input('Razão: '))
ultimo = primeiro + (10-1) * razao
for c in range(primeiro, ultimo + razao, razao):
    print(f'{c}', end=' ')

    