'''FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA(),
QUE RECEBA UM TEXTO QUALQUER COMO PARÂMETRO E MOSTRE UMA MENSAGEM COM
TAMANHO ADAPTÁVEL.'''

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f' {msg}')
    print(f'~' * tam)


escreva('Eu vou aprender programação.')
escreva('Tenho que ter calma e dedicação.')
escreva('Assim vou ter dinheiro para comprar um prato com macarrão.')
