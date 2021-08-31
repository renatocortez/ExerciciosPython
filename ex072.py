'''CRIE UM PROGRAMA QUE TENHA UMA TUPLA
TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO,
DE ZERO ATÉ VINTE.
O PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO(0-20)
E MOSTRÁ-LO POR EXTENSO.'''

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
'sete', 'oito', 'nove','dez', 'onze','doze', 'treze', 'catorze',
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente!', end='')
print(f'Você digitou o número {cont[num]}')

