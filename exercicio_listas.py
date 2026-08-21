numeros = [4, 7, 12, 15, 20, 3, 8, 11]
pares = 0
impares = 0
somap = 0
somai = 0
for i in numeros:
    if i % 2 == 0:
        pares = pares + 1
        print("Pares:", i)
        somap = somap + i
    else:
        impares = impares + 1
        print("Impares:", i)
        somai = somai + i
    


print(f"""
Pares = {pares}
Impares = {impares}
Soma dos Pares = {somap}
Soma dos Impares = {somai}""")