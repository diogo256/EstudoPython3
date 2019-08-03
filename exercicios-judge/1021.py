troco = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

if(troco > 0):
    rest = 0
    print("Notas:")
    for p in notas:
        if(troco >= p):
            n = int(troco/p)
            r = troco - p*n
            print('%s nota(s) de R$ %s.00' % (n, p))
            troco = r
        else:
            print('0 nota(s) de R$ %s.00' % p)
    for j in moedas:
        print(troco)