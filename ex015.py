'''ESCREVA UM PROGRAMA QUE PERGUNTE A
QUANTIDADE DE KM PERCORRIDOS POR UM CARRO
ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE
FOI ALUGADO.CALCULE O PREÇO A PAGAR, SABENDO
QUE O CARRO CUSTA R$60 POR DIA E r$0,15 POR KM
RODADO.'''

km = float(input('Quantos quilômetros foram percorridos? '))
dias = int(input('Quantos dias foram usados? '))
aluguel = (dias * 60) + (km * 0.15)
print('O total do valor a pagar pelo aluguel do carro é de R${}'.format(aluguel))

