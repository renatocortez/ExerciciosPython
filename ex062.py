print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
total = 0
cont = 1
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostras a mais? '))
print(f'PA finalizada com {total} termos.')

