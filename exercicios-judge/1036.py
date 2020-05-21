valores = input().split()
A, B, C = float(valores[0]), float(valores[1]), float(valores[2])

delta = 4*A*C
calcRaiz = ((B ** 2) - delta)
if A != 0 and calcRaiz > 0:
    R1 = (-B + (calcRaiz ** 0.5)) / (2*A)
    R2 = (-B - (calcRaiz ** 0.5))/ (2*A)
    print("R1 = %.5f" % R1)
    print("R2 = %.5f" % R2)
else:
    print("Impossivel calcular")