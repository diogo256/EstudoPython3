
#subprogramas
def calculoReajuste(reajustePorcent, valor):
    porcento = reajustePorcent/100
    valorPorcent = valor*porcento
    novoSalario = valorPorcent+valor
    print("Novo salario: %0.2f" % novoSalario)
    print("Reajuste ganho: %0.2f" % valorPorcent)
    print("Em percentual: ", reajustePorcent, "%")

def avaliaReajuste(valores):
    if(valores <= 400.00):
        calculoReajuste(15, valores)
    elif(valores > 400.00 and valores <= 800.00):
        calculoReajuste(12, valores)
    elif(valores > 800.00 and valores <= 1200.00):
        calculoReajuste(10, valores)
    elif(valores > 1200.00 and valores <= 2000.00):
        calculoReajuste(7, valores)
    elif (valores > 2000.00):
        calculoReajuste(4, valores)

#principal
valor = float(input())
avaliaReajuste(valor)
