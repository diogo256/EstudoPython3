import math

#subprograma
def buscarMenor(valores):
    menor = valores[0][0]
    global localF
    localF = valores[0][1]
    for indice in range(len(valores)):
        if menor > valores[indice][0]:
            menor = valores[indice][0]
            localF = valores[indice][1]
    return menor

#gravando localização das farmacias
dados = open("farmacias.txt", "w")
dados.write("300 200\n")
dados.write("10 56\n")
dados.write("25 41\n")
dados.write("90 18\n")
dados.write("70 90\n")
dados.write("100 50\n")
dados.close()


#Programa principal
dadosF = []
distanciaA = []
entrada = input("coordenadas ").split()

Leitura = open("farmacias.txt", "r")
L2 = Leitura.readline()

if L2 != "":
    vazio = 1
else:
    print("Arquivo de Farmácias está vazio!!!")
    vazio = 0

while L2 != "":

    dadosF.append(L2.split())

    L2 = Leitura.readline()

    vazio = 1

Leitura.close()

if vazio != 0:
    for indice in range(len(dadosF)):
        calculo = ((int(entrada[0]) - int(dadosF[indice][0])) ** 2) + ((int(entrada[1]) - int(dadosF[indice][1])) ** 2)
        distancia = math.sqrt(calculo)
        distanciaA.append([distancia, dadosF[indice][0] + " " + dadosF[indice][1]])

    encontraMenor = buscarMenor(distanciaA)
    print("Local da Farmácia Mais Próxima: ", localF)
    print("Distância à Percorrer: ", encontraMenor)