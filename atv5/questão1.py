valor = 0

while valor >= 0:
    valor = int(input("Informe um valor inteiro (digite um valor negativo para terminar): "))

    if valor > 10 and valor <= 100:
        print(f"O quadrado de {valor} é {valor*valor}")
    if valor > 5 and valor <= 10:
        print(f"O cubo de {valor} é {valor*valor*valor}")
    if valor > 100:
        print("Limite excedido.")

print("Programa Finalizado.")