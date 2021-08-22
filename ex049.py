'''REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O
USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR'''

print('-=' * 5, "Tabuada v2", "-=" * 5)

n = int(input('Digite um valor para saber a tabuada: '))
for c in range(0, 11):
    print(f"{n} x {c} = {n*c}")

