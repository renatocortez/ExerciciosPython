'''CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO
DE VÁRIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR
SE O USUÁRIO VAI CONTINUAR.
NO FINAL, MOSTRE:
1-TOTAL GASTO NA COMPRA
2-QUANTOS PRODUTOS CUSTAM MAIS DE R$1000
3-QUAL É O NOME DO PRODUTO MAIS BARATO'''

total = totmil = cont = menor = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar[S/N]?' )).upper().strip()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format('Fim do Programa'))
print(f'O total da compra foi R${total}')
print(f'Temos {totmil} produtos que custam mais de R$1.000')
print(f'O produto mais barato foi {barato} que custa R${menor}')
