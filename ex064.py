'''CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES (DESCONSIDERAND O FLAG(999)'''

n = soma = cont = 0
n = int(input('Digite um número[999 para parar]:'))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número[999 para parar:'))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
