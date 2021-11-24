frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra A aparece na {}º posição a primeira vez.'.format(frase.find('A')+1))
print('A letra A aparece na {}º posição a última vez.'.format(frase.rfind('A')+1))

