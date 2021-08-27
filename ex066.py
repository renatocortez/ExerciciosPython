'''CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS
INTEIROS PELO TECLADO.O PROGRAMA SÓ VAI PARAR QUANDO
O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE
PARADA. NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM
DIGITADOS E QUAL FOI A SOMA ENTRE ELES
(DESCONSIDERANDO O FLAG)'''

soma = contador = 0

while True:
    n = int(input('Digite um número[999 finaliza o programa]: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Foram digitados {contador} números, e a soma entre eles é igual a {soma}.')
