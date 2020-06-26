# coding: utf-8
import codecs
import re

#Arquivo de partidas
dados = open("partidas.txt", "w", encoding="utf8")
dados.write("4 3\n")
dados.write("OsBotões\n")
dados.write("LeoNoFutebol\n")
dados.write("Cacareco\n")
dados.write("ClubeDoJuca\n")
dados.write("OsBotões 6 x 0 Cacareco\n")
dados.write("Cacareco 0 x 2 ClubeDoJuca\n")
dados.write("Cacareco 0 x 2 LeoNoFutebol\n")
#dados.write("ClubeDoJuca 2 x 3 OsBotões\n")
dados.close()

#while linha != "":
#    print(linha, end="")
#    linha = Leitura.readline()
#print(linha)

#subprograma
#busca o arquivo
def buscaArquivo(nomeArquivo):
    # lendo arquivo
    Leitura = open(nomeArquivo, "r", encoding="utf8")
    linha = Leitura.readlines()
    global arrTimes
    arrTimes = []
    resultJogo = []
    for indice in range(len(linha)):
        #print(linha[indice])
        if indice == 0:
            linha1 = linha[indice].split()
            T = int(linha1[0])
            J = int(linha1[1])
            print("%d times e %d jogos" % (T, J))
        else:
            detalhaTimes = re.findall(r'\d+', str(linha[indice]))
            if detalhaTimes:
                resultado = linha[indice].split(" x ")
                resultJogo.append(resultado)
            else:
                arrTimes.append(linha[indice])
    #resultadoJogos(resultJogo,J)
    Leitura.close()
    return [resultJogo,J]

def resultadoJogos(jogos, quantPartidas):
    objResultado = []
    #array será composto [nomeTime, pontos, jogos, golsFeitos, golsSofridos, saldoGols]
    for indice in range(int(quantPartidas)):
        time1 = jogos[indice][0].split()
        time2 = jogos[indice][1].split()
        golsTime1 = time1[1]
        golsTime2 = time2[0]
        if int(golsTime1) > int(golsTime2):
            buscaTime1 = buscaElemento(objResultado, time1[0]) #busca o time1
            buscaTime2 = buscaElemento(objResultado, time2[1]) #busca o time2
            if buscaTime1 >= 0: #caso encontre o time
                objResultado[buscaTime1][1] = int(objResultado[buscaTime1][1]) + 3  # PontosVencidos
                objResultado[buscaTime1][2] = int(objResultado[buscaTime1][2]) + 1  # jogos
                objResultado[buscaTime1][3] = int(objResultado[buscaTime1][3]) + int(golsTime1) #golsFeitos
                objResultado[buscaTime1][4] = int(objResultado[buscaTime1][4]) + int(golsTime2) # golsSofridos
                objResultado[buscaTime1][5] = int(objResultado[buscaTime1][3]) - int(objResultado[buscaTime1][4]) #saldoGols
            else: #adiciona um novo time vencedor
                objResultado.append([time1[0], 3, 1, int(golsTime1), int(golsTime2), int(golsTime1)-int(golsTime2)])

            if buscaTime2 >= 0: #caso encontre o time derrotado
                objResultado[buscaTime2][1] = int(objResultado[buscaTime2][1]) + 0 # PontosVencidos
                objResultado[buscaTime2][2] = int(objResultado[buscaTime2][2]) + 1 # jogos
                objResultado[buscaTime2][3] = int(objResultado[buscaTime2][3]) + int(golsTime2) #golsFeitos
                objResultado[buscaTime2][4] = int(objResultado[buscaTime2][4]) + int(golsTime1) # golsSofridos
                objResultado[buscaTime2][5] = int(objResultado[buscaTime2][3]) - int(objResultado[buscaTime2][4])  # saldoGols
            else: #adiciona um novo time derrotado
                objResultado.append([time2[1], 0, 1, int(golsTime2), int(golsTime1), int(golsTime2)-int(golsTime1)])

        elif int(golsTime2) > int(golsTime1):
            buscaTime2 = buscaElemento(objResultado, time2[1])
            buscaTime1 = buscaElemento(objResultado, time1[0])
            if buscaTime2 >= 0:
                objResultado[buscaTime2][1] = int(objResultado[buscaTime2][1]) + 3  # PontosVencidos
                objResultado[buscaTime2][2] = int(objResultado[buscaTime2][2]) + 1  # jogos
                objResultado[buscaTime2][3] = int(objResultado[buscaTime2][3]) + int(golsTime2) # golsFeitos
                objResultado[buscaTime2][4] = int(objResultado[buscaTime2][4]) + int(golsTime1) # golsSofridos
                objResultado[buscaTime2][5] = int(objResultado[buscaTime2][3]) - int(objResultado[buscaTime2][4])  # saldoGols
            else:
                objResultado.append([time2[1], 3, 1, int(golsTime2), int(golsTime1), int(golsTime2)-int(golsTime1)])

            if buscaTime1 >= 0:
                objResultado[buscaTime1][1] = int(objResultado[buscaTime1][1]) + 0  # Partidas
                objResultado[buscaTime1][2] = int(objResultado[buscaTime1][2]) + 1  # jogos
                objResultado[buscaTime1][3] = int(objResultado[buscaTime1][3]) + int(golsTime1) #golsFeitos
                objResultado[buscaTime1][4] = int(objResultado[buscaTime1][4]) + int(golsTime2) # golsSofridos
                objResultado[buscaTime1][5] = int(objResultado[buscaTime1][3]) - int(objResultado[buscaTime1][4])  # saldoGols
            else:
                objResultado.append([time1[0], 0, 1, int(golsTime1), int(golsTime2), int(golsTime2)-int(golsTime1)])
    return objResultado

def buscaElemento(valores, procurado):
    local = -1
    for indice in range(len(valores)):
        nome = valores[indice][0]
        if nome==procurado:
            return indice
    return local

def trocar(vals, posX, posY):
    temp = vals[posX]
    vals[posX] = vals[posY]
    vals[posY] = temp
    return None

def selecionaMaior(vals, inicio, indice):
    localMaior = inicio
    for pos in range(inicio+1, len(vals)):
        if vals[pos][indice]>vals[localMaior][indice]:
            localMaior = pos
    return localMaior

def selecionaMenor(vals, inicio, indice):
    localMenor = inicio
    for pos in range(inicio+1, len(vals)):
        if vals[pos][indice]<vals[localMenor][indice] and vals[pos][5]==vals[localMenor][5]:
            localMenor = pos
    return localMenor

def ordernar(valores, indice):
    for ind in range(len(valores)-1):
        maior = selecionaMaior(valores, ind, indice)
        trocar(valores, ind, maior)
    return None

def ordernarAlfabeticamente(valores, indice):
    for ind in range(len(valores)-1):
        menor = selecionaMenor(valores, ind, indice)
        trocar(valores, ind, menor)
    return None

def criaTabela(obj):
    dados = open("tabela.txt", "w", encoding="utf8")

    for indice in range(len(obj)):
        dados.write("\n")
        for ind in range(len(obj[indice])):
            posicao = indice+1
            if ind == 0:
                dados.write("%d" % (posicao))
                if indice == 0:
                    dados.write("%11s" % "" + (obj[indice][ind]))
                elif indice == 3:
                    dados.write("%11s" % "" + (obj[indice][ind]))
                elif indice == 1:
                    dados.write("%8s" % "" + (obj[indice][ind]))
                else:
                    dados.write("%7s" % "" + (obj[indice][ind]))
            else:
                dados.write("%5d" % (obj[indice][ind]))

    dados.close()

#programa
partida = input()
encontra = buscaArquivo(partida)
ordenaClassificacao = resultadoJogos(encontra[0],encontra[1])
print(ordenaClassificacao)
ordernar(ordenaClassificacao, 1)
ordernar(ordenaClassificacao, 5)
ordernarAlfabeticamente(ordenaClassificacao, 0)
criaTabela(ordenaClassificacao)

#detalha =  re.findall(r'\d+', 'ab123')
#print(detalha)