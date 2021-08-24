'''MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI (PENSAR)
EM UM NÚMERO ENTRE 0 E 10. SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR
ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS'''

from random import randint
computador = randint(0, 10)

print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar?')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')


