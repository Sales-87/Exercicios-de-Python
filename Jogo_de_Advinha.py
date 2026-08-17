import random

jogador = True

print("===== Adivinhe o número =====")

while jogador:
    numero = random.randint(1, 10)
    contador = 0
    venceu = False

    while True:
        t = int(input("Digite um número de 1 a 10: "))

        if t > 10 or t < 1:
            print("Você errou...")
            print("Digite um número de 1 a 10!")
            continue

        contador = contador + 1

        if t == numero:
            print("Você Acertou!!🎉")
            venceu = True
            break

        else:
            print("Você errou🥺.")
            print(f"Tentativa {contador}")

            if t > numero:
                print("Dica: Menor 😏")
            elif t < numero:
                print("Dica: Maior 🤫")

            print("==============================")

        if contador == 5:
            print(f"Você perdeu! O número era {numero}")
            break

    if venceu:
        print(f"Você acertou em {contador} tentativas. Parabéns! 🔥")

    pergunt = int(input("""=============
Jogar novamente?
1 - Sim
2 - Não
: """))

    if pergunt == 1:
        continue

    elif pergunt == 2:
        jogador = False

print("Fim de jogo! 👋")
