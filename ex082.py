valores = list()
pares = list()
impares = list()

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar[S/N]? '))
    if resp in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {valores}.')
print(f'A lista de pares é {pares}.')
print(f'A lista de ímpares é {impares}.')
