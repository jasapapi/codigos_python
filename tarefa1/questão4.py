import random

while True:
    opcoes = ["Pedra", "Papel", "Tesoura"]
    
    computador = random.randint(1, 3)
    usuario = int(input("Escolha: (1) Pedra, (2) Papel, (3) Tesoura: "))

    if usuario not in [1, 2, 3]:
        print("Escolha inválida!")
        continue

    print(f"Você escolheu: {opcoes[usuario - 1]}")
    print(f"O computador escolheu: {opcoes[computador - 1]}")

    if usuario == computador:
        print("Empate!")
    elif (usuario - computador) % 3 == 1:
        print("Você venceu!")
    else:
        print("Computador venceu!")

    jogar_novamente = input("Jogar novamente? (s/n): ")
    if jogar_novamente != 's' and jogar_novamente != 'S':
        break