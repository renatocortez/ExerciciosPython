'''DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS.
NO FINAL MOSTRE:
1 - A MÉDIA DE IDADE DO GRUPO
2 - QUAL É O NOME DO HOMEM MAIS VELHO
3 - QUANTAS MULHERES TÊM MENOS DE 20 ANOS'''

somaIdade = 0
mediaIdade = 0
maiorHomem = 0
nomeVelho = 0
contMulher = 0

for c in range(1, 5):
    print(f'----- {c}ª pessoa -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: '))
    somaIdade += idade
    if c == 1 and nome in 'Mm':
        maiorHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorHomem:
        maiorHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        contMulher += 1
mediaIdade = somaIdade / 4
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'O {nomeVelho} é o homem mais velho com {maiorHomem} anos de idade.')
print(f'{contMulher} mulheres tem menos de 20 anos.')


