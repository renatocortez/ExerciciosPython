r1 = float(input('1ª reta: '))
r2 = float(input('2ª reta: '))
r3 = float(input('3ª reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo.')
    if r1 == r2 == r3:
        print('Os segmentos formam um triângulo Equilátero.')
    elif r1 != r2 != r3:
        print('Os segmentos formam um triângulo Escaleno.')
    else:
        print('Os segmentos formam um triângulo isósceles.')
else:
    print('Os segmentos não formam um triângulo. Tente novamente.')
    
