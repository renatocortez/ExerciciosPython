primeiro = int(input('1º termo: '))
razao = int(input('Razão: '))
ultimo = primeiro + (10-1) * razao
for c in range(primeiro, ultimo + razao, razao):
    print(f'{c}', end=' ')

    
