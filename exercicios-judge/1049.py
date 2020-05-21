def tipoAnimal(tipo):
    if tipo == 'ave':
        return 1
    elif tipo == 'mamifero':
        return 2
    elif tipo == 'inseto':
        return 3
    elif tipo == 'anelideo':
        return 4

def grupoAnimal(arrayTipo):
    if arrayTipo[0] == 'vertebrado':
        if tipoAnimal(arrayTipo[1]) == 1:
            if arrayTipo[2] == 'carnivoro':
                print('aguia')
            else:
                print('pombo')
        elif tipoAnimal(arrayTipo[1]) == 2:
            if arrayTipo[2] == 'onivoro':
                print('homem')
            else:
                print('vaca')
    else:
        if tipoAnimal(arrayTipo[1]) == 3:
            if arrayTipo[2] == 'hematofago':
                print('pulga')
            else:
                print('lagarta')
        elif tipoAnimal(arrayTipo[1]) == 4:
            if arrayTipo[2] == 'hematofago':
                print('sanguessuga')
            else:
                print('minhoca')

palavraLida = input()
arrayTipo = ()
while palavraLida != '':
    arrayTipo += (palavraLida,)
    if len(arrayTipo) == 3 :
        grupoAnimal(arrayTipo)
        palavraLida = ''
    else:
        palavraLida = input()