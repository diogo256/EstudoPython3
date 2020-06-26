
def construimatriz(linha, coluna, min, max):
    from random import randint
    vals = []
    for i in range(linha):
        novaLinha = []
        for j in range(coluna):
            novaLinha.append(randint(min, max))
        vals.append(novaLinha)
    return vals

def mostrar(vs):
    for i in range(len(vs)):
        for j  in range(len(vs[i])):
            print(vs[i][j], end=' ')
        print()
    print()
    return None

def linhaMaiorSoma(vs):
    def somar(vsLin):
        total = 0
        for x in vsLin:
            total += x
        return total

    maior = somar(vs[0])
    linhaMaior = 0
    for lin in range(1, len(vs)):
        somaAtual = somar(vs[lin])
        if somaAtual > maior:
            maior = somaAtual
            linhaMaior = lin
    for x in vs[linhaMaior]:
        print(x, end=" ")
    print()
    return None

linha = input().split(" ")
L, C = linha
valores = construimatriz(int(L), int(C), 10, 99)
mostrar(valores)
linhaMaiorSoma(valores)
