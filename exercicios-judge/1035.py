valores = input().split()
A, B, C, D = int(valores[0]), int(valores[1]), int(valores[2]), int(valores[3])

if B > C and A < D and (C + D) > (A + B) and (C > 0 and D > 0) and A%2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")