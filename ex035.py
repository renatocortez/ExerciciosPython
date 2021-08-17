'''DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE 3 RETAS E DIGA SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.
'''

r1 = float(input('1ª reta: '))
r2 = float(input('2ª reta: '))
r3 = float(input('3ª reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos de reta podem formar um triângulo.')
else:
    print('Os segmentos de reta não podem formar um triângulo.')
    