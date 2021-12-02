peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu imc é de {imc:.2f} e você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu imc é de {imc:.2f} e você está no peso ideal.')
elif 26 < imc < 30:
    print(f'Seu imc é de {imc:.2f} e você está com sobrepeso.')
elif 30 < imc < 40:
    print(f'Seu imc é de {imc:.2f} e você está com obesidade.')
else:
    print(f'Seu imc é de {imc:.2f} e você está com obesidade mórbida. Procure um médico.')
