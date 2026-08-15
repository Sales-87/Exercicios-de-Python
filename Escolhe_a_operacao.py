historico = []
while True:
    resp = int(input("""Escolha uma operação:
                 1 - Soma
                 2 - Subtração
                 3 - Multiplicação
                 4 - Divisão
                 5 - Potencia
                 0 - Sair
                 Digite a opção: """))
    if resp == 0:
        break

    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    calculo = False

    if resp == 1:
        resultado = n1 + n2
        print(f"Resultado: {resultado}")
        calculo = True
    elif resp == 2:
        resultado = n1 - n2
        print(f"Resultado: {resultado}")
        calculo = True
    elif resp == 3:
        resultado = n1 * n2
        print(f"Resultado: {resultado}")
        calculo = True
    elif resp == 4:
        if n2 == 0:
            print("Não é possível dividir por zero!")
        else:
            resultado = n1 / n2
            print(f"Resultado: {resultado:.2f}")
            calculo = True
    elif resp == 5:
        resultado = n1 ** n2
        print(f"Resultado: {resultado:.2f}")
        calculo = True
    else:
        print("Opção invalida tente novamente")

    if calculo:
        historico.append(resultado)

print(f"""Historico: 
         {historico}         """)
