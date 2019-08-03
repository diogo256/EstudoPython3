#Questão 6

# Subprogramas
def converte(numDecimal, base):
    if numDecimal < base:
        return str(numDecimal)
    else:
        return converte(numDecimal // base, base) + str(numDecimal % base)


# Programa Principal
numLido = input().split(" ")
while int(numLido[0]) != -1 and int(numLido[1]) != -1:
    print(converte(int(numLido[0]), int(numLido[1])), end=" ")
    print()
    numLido = input().split(" ")
