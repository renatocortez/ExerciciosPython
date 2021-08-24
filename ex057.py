'''FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES
[M] E [F]. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO'''

genero = str(input('Digite seu gênero[M/F]: ')).strip().upper()[0]
while genero not in 'MmFf':
    genero = str(input('Dados inválidos! Por favor, informe seu gênero[M/F]: ')).strip().upper()[0]
print(f'Gênero {genero} registrado com sucesso.')




