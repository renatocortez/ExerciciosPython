nome = str(input('Digite seu nome completo: '))
print('Seu nome em letras maiúsculas é:{}'.format(nome.upper()))
print('Seu nome em letras minúsculas é:{}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))

