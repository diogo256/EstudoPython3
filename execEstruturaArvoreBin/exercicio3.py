# AD1 - Questão 3

# Subprogramas

def gerar(nLins, nCols, min, max):
    from random import randint
    vals = [None] * nLins # outra possibilidade seria o uso de append dentro do laço
    for i in range(nLins):
        vals[i] = [0] * nCols # outra possibilidade seria o uso de append dentro do laço
        for j in range(nCols):
            vals[i][j] = randint(min, max)
    return vals


def mostrar(vals, linMin, linMax, colMin, colMax):
    for i in range(linMin, linMax):
        for j in range(colMin, colMax):
            print(vals[i][j], end=" ")
        print()
    print()
    return None


# Programa Principal
qtd = input().split()
qtdLinhas = int(qtd[0])
qtdColunas = int(qtd[1])
valores = gerar(qtdLinhas, qtdColunas, 100, 999)
mostrar(valores, 0, qtdLinhas, 0, qtdColunas)
