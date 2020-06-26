# AD1 - Questão 4

# Subprogramas

def converte(numDecimal, base):
    numConvertido = ""
    while numDecimal >= base:
        numConvertido = str(numDecimal % base) + numConvertido
        numDecimal = numDecimal // base
    numConvertido = str(numDecimal) + numConvertido
    return numConvertido

def converteDecimal(numBinario):
    numConvertido = str(numBinario)
    somaNum = 0
    potencia = len(numConvertido)-1
    for c in range(0, len(numConvertido)):
        calc = int(numConvertido[c]) * (2 ** potencia)
        potencia = potencia - 1
        somaNum += calc

    return somaNum


# Programa Principal
num = int(input())
while num != -1:
    numDecimal = converteDecimal(num)
    for b in range(3, 11):
        print(converte(numDecimal, b), end=" ")
    print()
    num = int(input())
