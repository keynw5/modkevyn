kk= 0
kk= 0
kk= 0
kk= 0
for i in range(1,5):
    tamanho = input("Informe o tamanho da camiseta: ")
    if tamanho == "P":
        kk += 1
    elif tamanho == "M":
        kk += 1
    elif tamanho == "G":
        kk += 1
    elif tamanho == "GG":
        kk += 1
    else:
        print("Tamanho inválido. Informe P, M, G ou GG.")
print("Total de camisetas:")
print("Tamanho P:", kk)
print("Tamanho M:", kk)
print("Tamanho G:", kk)
print("Tamanho GG:",kk)