
for n in range(1, 4):
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite outro numer: "))

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

par = int
if n1 % 2 == 0:
    par = par + 1

print(f"Temo {par} Pares")