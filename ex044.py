valor = float(input('Digite o valor do produto:R$ '))
print('''[1] - À VISTA(DINHEIRO OU CHEQUE) - 10% DE DESCONTO
[2] - À VISTA(CARTÃO DE DÉBITO/CRÉDITO) - 5% DE DESCONTO
[3] - 2X NO CARTÃO DE CRÉDITO - PREÇO NORMAL
[4] - 3X OU MAIS NO CARTÃO DE CRÉDITO - 20% DE JUROS''')
forma = int(input('Digite a opção escolhida: '))
opcao1 = valor - (valor * 10 / 100)
opcao2 = valor - (valor * 5 / 100)
opcao3 = valor
opcao4 = valor + (valor * 20 / 100)
if forma == 1:
    print(f'O valor do produto escolhido é de R${opcao1:.2f}.')
elif forma == 2:
    print(f'O valor do produto escolhido é de R${opcao2:.2f}.')
elif forma == 3:
    print(f'O valor do produto escolhido é de R${opcao3:.2f}.')
elif forma == 4:
    print(f'O valor do produto escolhido é de R${opcao4:.2f}.')
else:
    print(f'Opção inválida!!! Tente novamente.')




