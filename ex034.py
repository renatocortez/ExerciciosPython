'''ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO
E CALCULE O VALOR DO SEU AUMENTO PARA SALÁRIOS SUPERIORES A R$1.250,
CALCULE UM AUMENTO DE 10%, PARA INFERIORES OU IGUAIS CALCULE 15% DE AUMENTO.
'''

salario = float(input('Digite o valor de seu salário:R$ '))
if salario > 1250:
    aumento1 = salario + (salario * 10 / 100)
    print(f'O seu salário teve um aumento de 10% e o novo valor é de R${aumento1}.')
if salario <= 1250:
    aumento2 = salario + (salario * 15 / 100)
    print(f'O seu salário teve um aumento de 15% e o novo valor é de R${aumento2}.')


