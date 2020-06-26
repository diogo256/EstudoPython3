import random
def geraVetor():
    n = int(input())
    arrayGerado = [0] * n
    for i in range(n):
        arrayGerado[i] = random.random()
    return arrayGerado
def selecionaMenor(v, i):
    e=v

def troca(v, posX, posY):
    e=v

def ordenacao(v):
    for i in range(len(v)-1):
        menor = selecionaMenor(v, i)
        troca(v, i, menor)
    return None

nArray = geraVetor()
print(nArray)
ordenacao(nArray)