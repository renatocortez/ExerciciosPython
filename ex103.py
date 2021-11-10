'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), QUE RECEBA DOIS PARÂMETROS OPCIONAIS:O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU.O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE'''

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {n} fez {gol} gol(s) no campeonato.')

#PROGRAMA PRINCIPAL
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric:
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)



