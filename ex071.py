'''CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO
DE UM CAIXA ELETRÔNICO. NO INÍCIO, PERGUNTE AO
USUÁRIO QUAL SERÁ O VALOR A SER SACADO
E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA
VALOR SERÃO ENTREGUES
OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE
50, 20, 10 E 1'''

print('-=' * 20)
print('{:^30}'.format('Nublank'))
print('-=' * 20)
valor = int(input('Qual valor você quer sacar? '))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced} ')
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-=' * 30)
print('Obrigado. Volte sempre!')

