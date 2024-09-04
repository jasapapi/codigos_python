valor = float(input("Valor do produto: "))
formap = (input("Forma de pagamento: "))

if formap == "Pix" or "Dinheiro" or "Débito":
    print(f"O valor total com desconto é de {valor-(valor * 0.15):.2f} reais")

if formap == "Cartão de crédito à vista":
    print(f"O valor total com desconto é de {valor-(valor * 0.10):.2f} reais")

if formap == "Cartão de crédito pacelado em duas vezes":
    print(f"O valor é de duas vezes de {valor/2:.2f} reais")

if formap == "Cartão de crédito pacelado em três vezes":
    print(f"O valor é de três vezes de {(valor/3)+((valor/3)*0.10):.2f} reais")
        