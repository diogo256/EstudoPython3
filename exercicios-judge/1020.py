dias = int(input())

ano = dias // 365
mes = (dias - (ano*365))//30
dia = dias-(ano*365)-(mes*30)

print("%d ano(s)" % (ano))
print("%d mes(es)" % (mes))
print("%d dia(s)" % (dia))