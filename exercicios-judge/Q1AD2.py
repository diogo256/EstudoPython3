def calculoSoma (P1,Q2):
    arrayResposta = []
    if len(P) > len(Q):
        count = len(P1) - 1
        while count >= 0:
            menorZero = count-1
            if menorZero < 0:
                arrayResposta.append(P1[count])
            else:
                arrayResposta.append(P1[count] + Q2[count-1])
            count -=1
    return arrayResposta

P = input().split()
Q = input().split()

SOMA = calculoSoma(P,Q)

print(SOMA)
"""if len(P) > len(Q):
    R = len(P)-len(Q)
    while R != 0:
        Q.append(0)
        R -= 1
    print(P)"""

"""elif len(Q) > len(P):
    S = len(Q)-len(P)
    while S != 0:
        P.append(0)
        S -= 1
"""


