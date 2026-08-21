total = 0
pares = 0
impares = 0
soma = 0
primeiro = True
media = 0
maiormedia = 0
numeros = []
while True:
    n = int(input("Digite um numero: "))
    if  n == 0:
        break

    if primeiro:
        maior = n
        menor = n
        primeiro = False
    
    soma = soma + n
    total = total + 1

    if maior < n:
        maior = n
    if menor > n:
        menor = n

    if n % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    numeros.append(n)

media = soma / total
for numero in numeros:
    if numero > media:
        maiormedia = maiormedia + 1

print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Soma: {soma}")
print(f"Media: {media}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Voce digitou {total} numeros")
print(f"Numeros acima da media: {maiormedia}")

