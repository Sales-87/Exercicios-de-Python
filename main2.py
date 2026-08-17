numeros = []
soma = 0
pares = 0
impar = 0
for i in range(5):
    n = int(input("Digite um numero: "))
    if i == 0:
        maior = n
        menor = n
    numeros.append(n)
    soma = soma + n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if n % 2 == 0:
        pares = pares + 1
    else:
        impar= impar + 1
    
print(f"Numeros: {numeros}")
print(f"Soma = {soma}")
print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")
print(f"Pares = {pares}")
print(f"Impares = {impar}")