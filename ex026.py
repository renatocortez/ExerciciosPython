'''LEIA UMA FRASE E MOSTRE
1-QUANTAS VEZES APARECE A LETRA A
2-EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
3 - EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra A aparece na {}º posição a primeira vez.'.format(frase.find('A')+1))
print('A letra A aparece na {}º posição a última vez.'.format(frase.rfind('A')+1))

