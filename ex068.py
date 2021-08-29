'''FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR
COM O COMPUTADOR. O JOGO SÓ SERÁ INTERROMPIDO
QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL
DE VITÓRIAS CONSECUTIVAS QUE ELE CONQUISTOU NO
FINAL DO JOGO'''

from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar[P/I]? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
        break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
        else:
            print('Você perdeu!')
        break
print('Vamos jogar novamente.')
print(f'Game over. Você venceu {vitoria} vezes.')
        