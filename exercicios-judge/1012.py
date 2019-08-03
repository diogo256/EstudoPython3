# Programa Principal
linha1 = input().split(" ")
pi = 3.14159
a, b, c = linha1

TRIANGULO = (float(a) * float(c)) / 2
CIRCULO = pi * (float(c) ** 2)
TRAPEZIO = ( ( float(a) + float(b) ) * float(c) ) / 2
QUADRADO = (float(b) ** 2)
RETANGULO = float(a) * float(b)

print("TRIANGULO: %0.3f" % TRIANGULO)
print("CIRCULO: %0.3f" % CIRCULO)
print("TRAPEZIO: %0.3f" % TRAPEZIO)
print("QUADRADO: %0.3f" % QUADRADO)
print("RETANGULO: %0.3f" % RETANGULO)