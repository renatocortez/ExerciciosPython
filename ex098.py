'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(),
QUE RECEBA TRÊS PARÂMETROS: INÍCIO, FIM E PASSO. REALIZE A CONTAGEM.
-> SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO
CRIADA:
a) DE 1 ATÉ 10, DE 1 EM 1
b) DE 1O ATÉ 0, DE 2 EM 2
c) UMA CONTAGEM PERSONALIZADA
'''

from time import sleep

def contador(i, f , p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i 
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Personalize sua contagem agora!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)



