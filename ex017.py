'''LER O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM
TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA'''

from math import hypot
catop = float(input('Digite o comprimento do cateto oposto: '))
catadj = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(catop, catadj)
print('O comprimento da hipotenusa é de {:.2f}'.format(hipotenusa))
