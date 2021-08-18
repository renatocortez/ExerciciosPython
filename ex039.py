'''FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME,
DE ACORDO COM A SUA IDADE:
1-SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR
2-SE É A HORA DE SE ALISTAR
3-SE JÁ PASSOU DO TEMPO DO ALISTAMENTO
MOSTRAR TAMBÉM O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO
'''

from datetime import date

nasc = int(input('Ano de nascimento: '))
ano = date.today().year

if ano - nasc < 18:
    print(f'Ainda não está na idade para se alistar no serviço militar.Faltam {18 - (ano - nasc) } anos.')
elif ano - nasc == 18:
    print('Está na hora de se alistar para o serviço militar!')
else:
    print(f'Já passou da idade para se alistar no serviço militar.O prazo expirou em {(ano - nasc) - 18} anos.')

