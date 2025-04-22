sala = 1
salmin = float(input("Qual o salário mínimo atual: "))
while sala != 0:
    sala = float(input("Qual é o seu Salário: "))
    if sala == 0:
        break
    div = sala / salmin
    print(f"Você recebe {div} salários minimos")