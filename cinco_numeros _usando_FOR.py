positivo = 0
negativo = 0
zero = 0

for n in range(1, 6):
    numero = float(input("Digite um numero: "))

    if numero > 0:
        positivo = positivo + 1 

    if numero < 0:
        negativo = negativo + 1

    if numero == 0:
        zero = zero + 1

print(f"Quantidade de positivos = {positivo}")
print(f"Quantidade de negativos = {negativo}")
print(f"Quantidade de zeros = {zero}")