km = float(input('Quantos quilômetros foram percorridos? '))
dias = int(input('Quantos dias foram usados? '))
aluguel = (dias * 60) + (km * 0.15)
print('O total do valor a pagar pelo aluguel do carro é de R${}'.format(aluguel))

