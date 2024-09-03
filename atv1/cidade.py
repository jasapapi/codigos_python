cid = (input("Qual o nome da cidade? "))
dias = int (input("Quantos dias você permaneceu no local? "))
gasto = float (input("Qual o valor médio de gasto por dia? "))

total = (gasto*dias)

print(f"Você gastou um total de {total:.2f} reais na cidade {cid}.")
