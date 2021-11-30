from datetime import date

nasc = int(input('Ano de nascimento: '))
ano = date.today().year

if ano - nasc < 18:
    print(f'Ainda não está na idade para se alistar no serviço militar.Faltam {18 - (ano - nasc) } anos.')
elif ano - nasc == 18:
    print('Está na hora de se alistar para o serviço militar!')
else:
    print(f'Já passou da idade para se alistar no serviço militar.O prazo expirou em {(ano - nasc) - 18} anos.')

