distancia = float(input('Qual é a distância percorrida? '))
if distancia <= 200:
    preco = distancia * 0.50
    print(f'Você percorreu {distancia}km e o valor de sua passagem é de R${preco}.')
else:
    preco = distancia * 0.45
    print(f'Você percorreu {distancia}km e o valor de sua passagem é de R${preco}.')
