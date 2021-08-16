'''FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA
UM DOS DIGITOS SEPARADOS'''

n1 = int(input('Digite um número entre 0 e 9999: '))
n = str(n1)
print('unidade {}'.format(n[3]))
print('dezena {}'.format(n[2]))
print('centena {}'.format(n[1]))
print('milhar {}'.format(n[0]))


