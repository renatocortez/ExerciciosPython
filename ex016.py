'''NÚMERO REAL PARA SUA PORÇÃO INTEIRA'''

from math import trunc
n1 = float(input('Digite um número: '))
n2 = trunc(n1)
print('O número {} tem a porção inteira {}'.format(n1, n2))


