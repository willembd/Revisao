peso = float(input("Digite seu peso: "))
altura = float(input("Digite a altura: "))

imc = peso/altura**2

if imc < 18.6:
    print(f"{imc} Abaixo do peso")
elif imc >= 18.6 and imc <= 24.9:
    print(f"{imc} Peso ideal")
elif imc >= 25 and imc <= 29.9:
    print(f"{imc} Levemente acima do peso")
elif imc >= 30 and imc <= 34.9:
    print(f"{imc} Obesidade grau I")
elif imc >= 35 and imc <= 39.9:
    print(f"{imc} Obesidade grau II (Severa)")
else:
    print(f"{imc} Obesidade grau III (Mórbida)")