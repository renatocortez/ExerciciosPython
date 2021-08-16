'''ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
SE ELE ULTRAPASSAR 80 KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE
ELE FOI MULTADO. A MULTA VAI CUSTAR R$7 POR CADA KM ACIMA DO LIMITE'''

velocidade = int(input('Em qual velocidade você estava dirigindo na rodovia? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrapassou o limite máximo permitido(80km/h) e será multado em R${multa}.')
else:
    print('Parabéns, você está praticando a direção defensiva.')

    