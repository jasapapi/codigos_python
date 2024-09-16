import datetime 
ano = 2006

while ano >= 2006:
    AT = datetime.date.today()
    print(AT.year)
    ano = int(input("Digite o ano que você nasceu: "))

print(f"Você poderá participar do concurso!")