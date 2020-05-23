palavraLida = input()

if palavraLida == 'vertebrado':
    palavraLida = input()
    if palavraLida == 'mamifero':
        palavraLida = input()
        if palavraLida == 'onivoro':
            print('homem'.lower())
        else:
            print('vaca'.lower())
    else:
        palavraLida = input()
        if palavraLida == 'carnivoro':
            print('aguia'.lower())
        else:
            print('pomba'.lower())
else:
    palavraLida = input()
    if palavraLida == 'inseto':
        palavraLida = input()
        if palavraLida == 'herbivoro':
            print('lagarta'.lower())
        else:
            print('pulga'.lower())
    else:
        palavraLida = input()
        if palavraLida == 'onivoro':
            print('minhoca'.lower())
        else:
            print('sanguessuga'.lower())
