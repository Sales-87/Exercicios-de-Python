n = float(input("Digite o valor do saque: "))

if n <= 0:
    print("Valor invalido!")
elif n > 1000:
    print("Limite de saque excedido!")
else:
    print(f"Saque autorizado: R${n:.2f}")