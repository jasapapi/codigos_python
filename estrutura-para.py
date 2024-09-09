'''
Este código é uma representação do que acontece na maioria das linguagens de programação

for(contador=1; contador<=5; contador++){

}
'''

#1ª forma de operação do for
for contador in range(1,6):
    print(contador)

print("-"*40)   
#2ª forma de operação da for
for contador in range(1,11,2):# o 3º parâmetro indica com os valores serão incrementados(alteração de valor)
    print(contador)

print('-'*40)
#3ª forma da operação do for 
for contador in range(10,0,-1):
    print(contador,end=" ")# a função end informa como os valores serão exibidos ao final, por padão é dado um enter(\n)