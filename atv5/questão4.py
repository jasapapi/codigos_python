valor = 1
contador = 0
soma = 0
din = 0


while valor >= 1:
    valor = float(input(f"Produto {contador + 1}: R$ "))
    contador += 1
    soma += valor  
            
print (f"Total: R$ {soma:.2f}")

if din < soma:
    din = float(input("Dinheiro: R$ "))
    print(f"É necessário um valor maior que R$ {soma:.2f}")
    din = float(input("Dinheiro: R$ "))
if din >= soma:
    print(f"Troco: R$ {din - soma:.2f}")