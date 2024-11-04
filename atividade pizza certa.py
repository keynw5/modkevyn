pequeno=0
media=0
grande=0
total=0
maior = 0
menor = 999
while True: 
    pizza = str(input("qual tamanho da pizza que voce gostaria?")).upper().strip()
    if pizza == "P":
        total +=20
    if pizza == "M":
        total +=30
    if pizza == "G":
        total +=40
    acompanhamento = str(input('deseja um acompanhamento: s/n: ')).upper().strip()
    if acompanhamento == 'S':
        while True:
            sabor = str(input('escolha Ca/m/t/Ce/B: s/n: ')).upper().strip()
            if sabor == 'CA' or 'M' or 'T' or 'CE' or 'B':
                total += 5
            if sabor == "N":
                break
    bebida = str(input("deseja uma bebida s/n: ")).upper().strip()
    if bebida == "S":
        total+=8
    if maior < total:
        maior = total
    if menor > total:
        menor = total
    print = total
    pedido = str(input('Pedir outra pizza s/n: ')).upper().strip()
    if pedido == "N":
        break
