sal = float(input("Digite seu salário: "))

if sal < 1900:
    print("Você é isento de imposto.")

if sal >= 1901 and sal <= 2800:
    print(f"Você irá pagar {sal * 0.075:.2f} reais")

if sal >= 2801 and sal <= 3700:
    print(f"Você irá pagar {sal * 0.15:.2f} reais")

if sal > 3700:
    print(f"Você irá pagar {sal * 0.225:.2f} reais")