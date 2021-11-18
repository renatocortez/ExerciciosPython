print('$$$$$$ PREÇO COM DESCONTO DE 5% $$$$$$')
n = float(input('Digite o valor do produto:R$ '))
d = n - (n * 5 / 100)
print('O valor do produto com desconto de 5% é de R${:.2f}'.format(d))
