conta = float(input("Digite o valor da conta: R$ "))
porcentual = float(input("Digite o porcentual de gorjeta (10, 15 ou 20): "))

gorjeta = conta * (porcentual / 100)
total = conta + gorjeta

print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Total: R$ {total:.2f}")