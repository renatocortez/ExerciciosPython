'''CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO() QUE VAI
RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA,
RETORNANDO UM VALOR LITERAL INDICANDO SE UMA PESSOA TEM VOTO
NEGADO, OPCIONAL OU OBRIGATÓRIO NAS ELEIÇÕES'''

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

