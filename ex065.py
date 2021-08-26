'''CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES E QUAL FOI O
MAIOR E O MENOR VALORES LIDOS.
O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR'''

resposta = 'S'
soma = quantidade = media = maior = menor = 0

while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
media = soma / quantidade
print(f'Você digitou {quantidade} números e a média é igual a {media:.2f}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')


