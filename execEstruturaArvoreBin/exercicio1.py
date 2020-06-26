entrada = input()

maior = 0.0
quantStringNaoVazia = 0
somatorio = 0.0

while(entrada != ""):
    if( entrada.isdigit()):
        if maior < float(entrada):
            maior = float(entrada)
        somatorio += float(entrada)
        quantStringNaoVazia += 1
    entrada = input()

print(maior)
print(quantStringNaoVazia)
print(somatorio/quantStringNaoVazia)