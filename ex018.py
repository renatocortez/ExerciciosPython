from math import sin, cos, tan, radians

valor = float(input('Digite um valor de ângulo qualquer: '))
seno = sin(radians(valor))
cosseno = cos(radians(valor))
tangente = tan(radians(valor))
print('O valor do seno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(seno, cosseno, tangente))
