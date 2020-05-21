
#subprogramas
def calculoReajuste(valor):
    valorFinal = 0.0
    reajuste = 0.0
    valorReajuste = 0.0
    if valor <= 400:
        reajuste = 15
        valorReajuste = valor * 0.15
        valorFinal = valor + valorReajuste
    elif valor <= 800:
        reajuste = 12
        valorReajuste = valor * 0.12
        valorFinal = valor + valorReajuste
    elif valor <= 1200:
        reajuste = 10
        valorReajuste = valor * 0.10
        valorFinal = valor + valorReajuste
    elif valor <= 2000:
        reajuste = 7
        valorReajuste = valor * 0.07
        valorFinal = valor + valorReajuste
    else:
        reajuste = 4
        valorReajuste = valor * 0.04
        valorFinal = valor + valorReajuste
    return valorFinal, valorReajuste, reajuste



#principal
valor = float(input())
valorReajustado, valorReajuste, reajuste = calculoReajuste(valor)
print("Novo salario: %.2f" % valorReajustado)
print("Reajuste ganho: %.2f" % valorReajuste)
print("Em percentual:",reajuste, "%")
