#Questão 5

arrayPonto = []
qtdParesLidos = 0
linhaLida = input()  # faz a leitura da primeira linha
if(linhaLida.split()[0] != 0 or linhaLida.split()[1] != 0):
    arrayPonto.append(linhaLida.split())

while linhaLida.split()[0] != 0 or linhaLida.split()[1] != 0:  # repete até que o ponto 0 0 seja lido
    qtdParesLidos = qtdParesLidos + 1
    linhaLida = input()  # faz a leitura da próxima linha
    if (linhaLida.split()[0] != 0 or linhaLida.split()[1] != 0):
        arrayPonto.append(linhaLida.split())