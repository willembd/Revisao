n = int(input("Digite um número: "))

if n % 2 == 0 and n >0:
    print(f"O {n} é Par e Positivo")
elif n % 2 == 0 and n < 0:
    print(f"O {n} é Par e Negativo")
elif n % 2 == 1 and n > 0:
    print(f"O {n} é Impar e Positivo")
else:
    print(f"O {n} é Impar e Negativo")