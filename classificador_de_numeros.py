positivo = 0
negativo = 0
zero = 0

for n in range(1, 6):
     num = float(input("Digite um numero: "))

     if num > 0:
      print("Positivo")
      positivo += 1
     elif num < 0:
       print("Negativos")
       negativo += 1
     else:
      print("Zero")
      zero += 1
 
print(f"Positivo = {positivo}")
print(f"Negativos = {negativo}")
print(f"Zero = {zero}")
