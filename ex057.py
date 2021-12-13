genero = str(input('Digite seu gênero[M/F]: ')).strip().upper()[0]
while genero not in 'MmFf':
    genero = str(input('Dados inválidos! Por favor, informe seu gênero[M/F]: ')).strip().upper()[0]
print(f'Gênero {genero} registrado com sucesso.')




