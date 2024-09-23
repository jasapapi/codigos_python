import time

seg = int (input("informe a quantidade de segundos: "))

for i in range (seg, -1, -1):
    print (f" {i} segundo restantes")
    time.sleep (1)

print ("Tempo esgotado!")