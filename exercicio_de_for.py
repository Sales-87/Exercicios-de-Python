n = int(input("Digite um numero: "))
somapar = 0
somaimp = 0
impar = 0
par = 0
for num in range(1, n + 1):
    if num % 2 == 0:
      somapar = somapar + num
      par = par + 1
    if num % 2 == 1:
       somaimp = somaimp + num 
       impar = impar + 1

print(f"""Pares = {par}
Impares = {impar}
Soma dos Pares= {somapar}
Soma dos Impares= {somaimp}""")

