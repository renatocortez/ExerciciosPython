maior = 0
menor = 0

listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}:'))) #ADICIONA VALORES NA LISTA
    if c == 0: #QUANDO C FOR O PRIMEIRO VALOR LIDO
        maior = menor = listanum[c] # ELE É O MAIOR E O MENOR
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum): #VARRE A LISTA PARA ACHAR AS POSIÇÕES DOS VALORES
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
print()
