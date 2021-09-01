'''Crie um programa que tenha uma tupla única com
nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

listagem = ('Arroz', 10, 'Queijo', 14, 'Vinho', 30,
             'Manteiga', 10, 'Cogumelos', 15)

print('-=' * 20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-=' * 20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-=' * 20)


