#Questão 4

# Subprogramas
def gerar(qL, qC):
    from random import randint
    vals = []
    for lin in range(qL):
        linha = []
        for col in range(qC):
            linha.append(randint(0, 9))
        vals.append(linha)
    return vals

def mostrar(vals):
    for lin in vals:
        for x in lin:
            print(x, end=" ")
        print()
    return None



# Programa Principal
qtdLinhas = int(input("Digite a quantidade de linhas: "))
qtdColunas = int(input("Digite a quantidade de colunas: "))

valores = gerar(qtdLinhas, qtdColunas)

#(a) A matriz gerada aleatoriamente;
print()
print("Matriz Gerada Aleatoriamente:")
mostrar(valores)