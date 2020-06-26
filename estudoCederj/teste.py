#subprogramas
def preencher(valores):
    for ind in range(len(valores)):
        valores[ind] = int(input("Elemento["+str(ind)+"]="))
    return None

def buscaElemento(valores, procurado):
    print(valores)
    for indice in range(len(valores)):
        if valores[indice]==procurado:
            return indice
    return -1

def buscaElemento2(valores, procurado):
    inicio = 0
    fim = len(valores)-1
    meio = (inicio + fim)//2
    while (inicio<fim) and (procurado!=valores[meio]):
        if procurado>valores[meio]:
            inicio = meio+1
        else:
            fim = meio-1
        meio=(inicio+fim)//2
    if procurado!=valores[meio]:
        local = -1
    else:
        local = meio
    return local

def escreverResposta(valor, pos):
    if pos<0:
        print(valor, "não encontrado")
    else:
        print(valor, "foi encontrado na posição", pos)
    return

#principal
numeros = [0]*10
preencher(numeros)
dado = int(input("escolha"))
onde = buscaElemento2(numeros, dado)
escreverResposta(dado, onde)