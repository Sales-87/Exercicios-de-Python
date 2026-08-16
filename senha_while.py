contador = 1
while True:
    s = int(input("Digite a senha: "))
    contador = contador + 1

    if s == 1234:
        print("Acesso permitido!")
        break
    elif contador == 4:
        print("Acesso bloqueado!")
        break
    else:
        print("Senha incorreta!")

    
