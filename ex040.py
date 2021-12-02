n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print(f'Sua média é igual a {media} e você está APROVADO!Parabéns!')
elif  5 <= media <= 6.9:
    print(f'Sua média é igual a {media}.Você está em RECUPERAÇÃO!Se prepare!')
elif media < 5:
    print(f'Sua média é igual a {media}.Infelizmente você está REPROVADO!Revise seus erros, estude mais!')


