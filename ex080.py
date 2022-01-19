lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #SE O VALOR É O PRIMEIRO OU O ÚLTIMO
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:#SENÃO ELE ENTRA NA POSIÇÃO ENTRE O PRIMEIRO E O ÚLTIMO
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print('-_-' * 20)
print(f'Os valores digitados em ordem foram {lista}')
