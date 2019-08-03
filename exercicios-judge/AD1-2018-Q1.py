#AD1 2018/1

arrNumber = []

def grava(numero):
    if len(arrNumber) < 6:
        arrNumber.append(numero)
    else:
        numLido = -1
    return arrNumber

# Programa Principal
numLido = int(input())
while numLido < 0:
    print(grava(numLido), end=" ")
    print()
    numLido = int(input())