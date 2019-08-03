n = int(input())

horas = n // 3600
minutos = (n - (horas*3600)) // 60
segundos = n - (horas*3600) - (minutos*60)


print("%d:%d:%d" % (horas, minutos, segundos))