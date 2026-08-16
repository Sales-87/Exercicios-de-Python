soma = 0
media = 0
for num in range(5):
    n = int(input("Digite um numero: "))
    if num == 0:
       maior = n
       menor = n
    soma = soma + n
    media = soma / 5
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f"Soma = {soma}")
print(f"Media = {media}")    
print(f"Maior = {maior}")
print(f"Menor = {menor}")