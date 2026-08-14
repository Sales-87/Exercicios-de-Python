n1 = float(input("Digite o Primeiro Numero: "))
n2 = float(input("Digite o Segundo Numero: "))
soma = n1 + n2
menos = n1 - n2
multipli = n1 * n2
opcao = input("Escolha uma opção [+],[-],[*]")

if opcao == "+":
        print(f"O resultado da Soma foi: {soma}")
elif opcao == "-":
        print(f"O resultado da Subtração foi: {menos} ")
elif opcao == "*":
        print(f"O resultado da Multiplicação foi: {multipli}")
else:
        print("ERRO DIGITE CORRETAMENTE!")
        


