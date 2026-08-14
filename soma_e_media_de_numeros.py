media = 0
soma = 0

for n in range(1,6):
    num = float(input("Digite um numero: "))

    soma = soma + num

media = soma / 5
print(f"Soma = {soma:.2f}")
print(f"Média = {media:.2f}")