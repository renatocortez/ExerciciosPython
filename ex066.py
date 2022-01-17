soma = contador = 0

while True:
    n = int(input('Digite um número[999 finaliza o programa]: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Foram digitados {contador} números, e a soma entre eles é igual a {soma}.')
