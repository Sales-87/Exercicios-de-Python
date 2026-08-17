historico = []
while True:
    resp = int(input("""Escolha uma operação:
                 1 - Soma
                 2 - Subtração
                 3 - Multiplicação
                 4 - Divisão
                 5 - Potencia
                 6 - Historico
                 7 - Limpar Historicop
                 0 - Sair
                 Digite a opção: """))
    if resp == 0:
        break
    if resp == 6:
        if not historico:
            print("Nenhuma operação realizada!")
            continue
        print("===== HISTORICO =====")
        for operacao in historico:
            print(operacao)
        print("=====================")
        continue
    if resp < 0 or resp > 7:
        print("Opção invalida tente novamente")
        continue
    if resp == 7:
        historico.clear()
        print("Histórico apagado!")
        continue

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
        resultado = n1**n2
        print(f"Resultado: {resultado:.2f}")
        calculo = True

    if calculo:
        if resp == 1:
            historico.append(f"{n1} + {n2} = {resultado}")
        elif resp == 2:
            historico.append(f"{n1} - {n2} = {resultado}")
        elif resp == 3:
            historico.append(f"{n1} x {n2} = {resultado}")
        elif resp == 4:
            historico.append(f"{n1} / {n2} = {resultado}")
        elif resp == 5:
            historico.append(f"{n1} ** {n2} = {resultado}")

print("===== HISTORICO =====")
for operacao in historico:
    print(operacao)
print("=====================")
