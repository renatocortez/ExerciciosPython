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


