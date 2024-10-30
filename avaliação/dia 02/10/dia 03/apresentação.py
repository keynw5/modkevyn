#ESCREVER UM ALGORITMO QUE LEIA 50 NUMEROS E INFOME QUANTOS DESTES VALORES SAO NEGATIVOS
CONTAR=1
CONTAR=2
for i in range (1,51):
    f1=int(input("digite um numero"))
    if (f1< 0):
        contar1=contar1+1
    else:
        contar2= contar2+1
print("o valor é negativo", contar1)
print("o valor é positivo", contar2) 