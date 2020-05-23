p1, p2, p3, p4 = input().split()

peso_1, peso_2, peso_3, peso_4 = 2,3,4,1

mp = ((float(p1) * peso_1) + (float(p2) * peso_2) + (float(p3) * peso_3) + (float(p4) * peso_4)) / (peso_1 + peso_2 + peso_3 + peso_4)

print("Media: %.1f" % mp)

if mp >= 5.0 and mp <= 6.9:
    print("Aluno em exame.")
    exame = float(input())
    mediaFinal = (mp + exame) / 2
    if mediaFinal >= 5.0:
        print("Nota do exame: %.1f" % exame)
        print("Aluno aprovado.")
    else:
        print("Nota do exame: %.1f" % exame)
        print("Aluno reprovado.")
    print("Media final:  %.1f", mediaFinal)
elif mp > 70:
    print("Media: %.1f" % mp)
    print("Aluno aprovado.")
else:
    print("Media: %.1f" % mp)
    print("Aluno reprovado.")





