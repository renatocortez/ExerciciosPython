'''ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA
PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
1-BINÁRIO
2-OCTAL
3 – HEXADECIMAL'''

n = int(input('Digite um número: '))
print('Opções:\n(1) - Binário\n(2) - Octal\n(3) - Hexadecimal')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    print(f'{n} convertido para binário é igual a {bin(n)[2:]} ')
elif opcao == 2:
    print(f'{n} convertido para octal é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} convertido para hexadecimal é igual a {hex(n)[2:]}')
else:
    print('Opção inválida.Tente novamente.')

