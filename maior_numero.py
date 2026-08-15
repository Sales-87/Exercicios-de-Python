n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numero: "))

if n1 > n2 and n1 > n3:
    print(f"O maior numero é {n1}")
elif n2 > n3:
    print(f"O maior numero é {n2}")
else: 
    print(f"O maior numero é {n3}")

if n1 < n2 and n1 < n3:
    print (f"O menor numero é {n1}")
elif n2 < n3:
    print(f"O menor numero é {n2}")
else:
    print(f"O menor numero é {n3}")

par = 0
imp = 0
if n1 % 2 == 0:
    par = par + 1

if n2 % 2 == 0:
    par = par + 1

if n3 % 2 == 0:
    par = par + 1

if n1 % 2 == 1:
    imp = imp + 1

if n2 % 2 == 1:
    imp = imp + 1

if n3 % 2 == 1:
    imp = imp + 1

print(f"Temos {par} numeros Pares")
print(f"Temos {imp} numeros Impares")