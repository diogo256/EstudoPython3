
def fib(n):
    global cont, conter
    if n == 0:
        cont = cont + 1
        return 0
    if n == 1:
        cont = cont + 1
        conter = conter + 1
        return 1
    else:
        cont = cont + 1
        return fib(n-1)+fib(n-2)

n = int(input())

for i in range(n):
    a = int(input())
    cont = -1
    conter = 0
    f = fib(a)
    print('fib(%i) = %i calls = %i' % (a, cont, conter))

