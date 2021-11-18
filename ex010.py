print('$$$ CONVERSOR DE REAL PARA DÓLAR $$$')
n = float(input('Digite o valor que deseja fazer a conversão: '))
d = n / 5.65
print('O valor de R${} reais equivale a US${:.2f} dólares'.format(n, d))
