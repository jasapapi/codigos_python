def total_calorias (atividade, tempo):
    if atividade == "caminhada":
        return tempo * 5
    
    elif atividade == "corrida":
        return tempo * 10
    
    elif atividade == "ciclismo":
        return tempo * 8
    
    else:
        return None
    
atividade = input("Digite o tipo de atividade (caminhada, corrida ou ciclismo): ")
tempo = int(input("Digite o tempo em minutos: "))

calorias = total_calorias(atividade, tempo)

if calorias is not None:
        print(f"Você queimou {calorias} calorias.")
else: 
        print("Atividade inválida.")
