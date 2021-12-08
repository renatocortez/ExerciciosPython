contmaior = 0
contmenor = 0

from datetime import date
ano = date.today().year
for c in range(1, 8):
    nasc = int(input('Ano de nascimento: '))
    idade = ano - nasc
    if idade >= 18:
        contmaior += 1
    else:
        idade < 18
        contmenor += 1
print(f'{contmaior} pessoas são maiores de idade.')
print(f'{contmenor} pessoas são menores de idade.')

