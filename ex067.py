'''FAÇA UM PROGRAMA QUE MOSTRE A TABUADA
DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA
VALOR DIGITADO PELO USUÁRIO. O PROGRAMA SERÁ
INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR
NEGATIVO.'''

print('& & & Tabuada 3.0v & & &')
while True:
    n = int(input('Digite o valor da tabuada desejada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')

print('Número inválido!Tente novamente.')