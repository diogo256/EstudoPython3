entrada = input()

def buscaModa(valores):
    auxiliar = [0]*len(valores)
    for indice in range(len(valores)): # calcula as frequências
        auxiliar[indice] = 1
        for varre in range(indice+1, len(valores)):
            if valores[varre]==valores[indice]:
                auxiliar[indice] += 1
    ondeModa = 0
    for i in range(1, len(auxiliar)): # localiza a maior frequência
        if auxiliar[i] > auxiliar[ondeModa]:
            ondeModa = i
    return valores[ondeModa], auxiliar[ondeModa]

if entrada == '':
    print("nenhum número foi lido!!!")
else:
    arrayNumero = entrada.split()
    valor, repeticao = buscaModa(arrayNumero)
          
    print("Valor que mais ocorreu: ", float(valor), "que foi encontrado: ",repeticao, "vez(es)")

