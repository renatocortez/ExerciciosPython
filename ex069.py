contador18 = contadorh = contadorm = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        contador18 += 1
    if sexo in 'M':
        contadorh += 1
    if sexo in 'F' and idade < 20:
        contadorm += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar[S/N] ?')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'{contador18} pessoas tem mais de 18 anos.')
print(f'{contadorh} homens foram cadastrados.')
print(f'{contadorm} mulheres tem menos de 20 anos.')



