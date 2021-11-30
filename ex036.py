casa = float(input('Valor do ímovel que deseja financiar:R$ '))
salario = float(input('Salário do responsável pelo financiamento:R$ '))
anos = int(input('Quantidade de anos que deseja para pagar: '))

prestacao = casa / (anos * 12)

if prestacao <= salario * ( 30 / 100 ):
    print(f'O total de parcelas do financiamento é de { anos * 12 }, o valor de cada parcela é de R${prestacao:.2f}.')
else:
    print(f'O valor de cada parcela é de R${prestacao:.2f}, ela não pode exceder 30% de seu salário, e por isso, o empréstimo foi NEGADO!')


