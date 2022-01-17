print('& & & Tabuada 3.0v & & &')
while True:
    n = int(input('Digite o valor da tabuada desejada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')

print('Número inválido!Tente novamente.')
