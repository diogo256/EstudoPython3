#Questão 2

leia = input()

#(a) a quantidade de vogais lidas;
def verificaPalíndrome(string):
    reversedStr = ''
    for ch in string[::-1]:
        reversedStr = reversedStr + ch
    if(string == reversedStr):
        return True
    else:
        return False

vogais = ['a', 'e', 'i', 'o', 'u']
letrasSemEspaco = leia.replace(" ", "")
cont = 0
for i in range(len(letrasSemEspaco)):
    if letrasSemEspaco[i].lower() in vogais:
        cont = cont+1
print(cont, "vogais lidas")

#(b) a quantidade de dígitos lidos;
digitos = leia.replace(" ", "")
print(len(digitos), "dígitos lidos")

#(c) qual foi a string de maior comprimento lida. Caso haja empate, escreva uma delas;
arrDigitos = leia.split(" ")
maiorString = ""
for i in range(len(arrDigitos)):
    temp = len(arrDigitos[i])
    if(temp >= len(maiorString)):
        maiorString = arrDigitos[i]
print(maiorString, " - foi a string de maior comprimento lida")

#(d) a quantidade de strings palíndromes lidas.
arrLeia = leia.split(" ")
count = 0
for i in range(len(arrLeia)):
    if verificaPalíndrome(arrLeia[i].lower()):
        count = count+1
print(count, "strings palíndromes lidas")