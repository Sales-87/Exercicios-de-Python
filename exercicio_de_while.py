t = 0
soma = 0
positivo = 0 
negativo = 0
maior = 0
menor = 0
while True:
    n = int(input("Digite um numero: "))

    if n == 0:
        break
    if n > 0:
        positivo = positivo + 1
    elif n < 0:
        negativo = negativo + 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    
    t = t + 1
    soma = soma + n

print(f"Voce digitou {t} numeros.")
print(f"Soma = {soma}")
print(f"Positivos = {positivo}")
print(f"Negativos = {negativo}")
print(f"Maior = {maior}")
print(f"Menor = {menor}")