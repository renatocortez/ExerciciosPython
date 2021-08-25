'''CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
1 - SOMAR
2 - MULTIPLICAR
3 - MAIOR
4 - NOVOS NÚMEROS
5 - SAIR DO PROGRAMA
O PROGRAMA DEVERÁ REALIZAR AS OPERAÇÕES ACIMA'''

from time import sleep
n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
opcao = 0
while opcao != 5:
    print('''\n[1] - SOMAR\n[2] - MULTIPLICAR\n[3] - MAIOR NÚMERO\n[4] - NOVOS NÚMEROS\n[5] - SAIR''')
    print('-=' * 20)
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma dos números {n1} e {n2} é igual a {soma}.')
    elif opcao == 2:
        multi = n1 * n2
        print(f'O número {n1} multiplicado por {n2} é igual a {multi}.')
    elif opcao == 3:
        if n1 > n2:
            print(f'O número {n1} é o maior.')
        else:
            print(f'O número {n2} é o menor.')
    elif opcao == 4:
        n1 = int(input('1º valor: '))
        n2 = int(input('2º valor: '))
    elif opcao == 5:
        print('Finalizando....')
    else:
        print('Opção inválida!Tente novamente.')
    print('-=' * 20)
    sleep(2)
print('Fim do programa. Obrigado.')
