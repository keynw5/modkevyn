#faça um programa que receba a idade, altura e o peso de 25 pessoas e mostre a quantidade de pessoas com idade superior a 50 ano.
contador=0
i=0
while(i<5):
    i+=1
    idade=int(input("informe a idade"))
    altura=float(input("informe a altura"))
    peso=float(input("informe o peso"))
    if (idade > 50):
        contador=+1

print(contador)