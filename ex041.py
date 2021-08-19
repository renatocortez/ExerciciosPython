'''CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE
SUA CATEGORIA, DE ACORDO COM A IDADE:
1-ATÉ 9 ANOS: MIRIM
2-ATÉ 14 ANOS: INFANTIL
3-ATÉ 19 ANOS:JUNIOR
4-ATÉ 25 ANOS: SENIOR
5 - ACIMA: MASTER'''

from datetime import date
ano = date.today().year

nasc = int(input('Digite o ano de seu nascimento: '))
idade = ano - nasc

if idade <= 9:
    print('Você é da categoria Mirim.')
elif 9 < idade <= 14:
    print('Você é da cateria Infantil.')
elif 14 < idade <= 19:
    print('Você é da categoria Junior.')
elif 19 < idade <= 25:
    print('Você é da categoria Sênior.')
else:
    print('Você é da categoria Master.')


