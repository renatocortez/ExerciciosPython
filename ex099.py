'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VÁRIOS PARÂMETROS COM VALORES INTEIROS.
SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR.'''

#Parâmetros Empacotados

from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados....')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


#Programa principal
maior(2, 5, 7, 1, 3, 7)
maior(9, 4, 12)
maior(1, 2)
maior(6)

