'''UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA
APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E
ESCREVENDO O NOME ESCOLHIDO'''

from random import choice
a1 = input('1° Aluno: ')
a2 = input('2° Aluno: ')
a3 = input('3° Aluno: ')
a4 = input('4° Aluno: ')
lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print('O aluno escolhido foi {}'.format(sorteio))


