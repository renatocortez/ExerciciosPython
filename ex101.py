def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com idade de {idade} anos: Voto proibido.'
    if 16 <= idade < 18 or idade > 65:
        return f'Com idade de {idade} anos: Voto opcional.'
    else:
        return f'Com idade de {idade} anos: Voto obrigatório.'


nasc = int(input('Digite o ano de seu nascimento: '))
print(voto(nasc))

