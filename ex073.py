'''CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS
COLOCADOS DO CAMPEONATO BRASILEIRO, NA ORDEM
DE COLOCAÇÃO E MOSTRE:
1-APENAS OS 5 PRIMEIROS COLOCADOS
2-OS ÚLTIMOS 4 COLOCADOS
3-UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA
4-EM QUE POSIÇÃO ESTÁ O SANTOS'''

times = ('Fortaleza', 'Atlético-PR', 'Flamengo', 'Atlético-GO', 'Atlético-MG',
         'Bragantino', 'Fluminense', 'Bahia', 'Palmeiras', 'Corinthians', 'Ceará', 'Santos', 'Internacional',
         'Juventude','Cuiabá', 'Sport', 'São Paulo', 'Chapecoense', 'Grêmio', 'América-MG')

print(f'Os cinco primeiro colocados são{times[0:5]}')
print(f'Os 4 últimos colocados são {times[-4:]}')
print(f'Os times em ordem alfabética :{sorted(times)}')
print(f'O time do Santos está na {times.index("Santos")+1}ª posição.')