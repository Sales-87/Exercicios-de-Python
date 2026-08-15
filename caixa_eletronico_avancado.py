s = int(input("Valor do saque: "))
cem = s // 100
resto = s % 100

cinquenta = resto // 50
resto = resto % 50

vinte = resto // 20
resto = resto % 20

dez = resto // 10

print(f"Nota de 100 : {cem}")
print(f"Nota de 50 : {cinquenta}")
print(f"Nota de 20 : {vinte}")
print(f"Nota de 10 : {dez}")