n = int(input("Digite um numero: "))
par = 0
impar = 0
soma = 0
for num in range(1, n + 1):
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    soma = soma + num

print(f"Pares: {par}")
print(f"Imapares: {impar}")
print(f"Soma: {soma}")