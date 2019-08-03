x = 0


def fib(n):
    global x
    x = x + 1
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


N = input()
A = []
if int(N) > 1:
    while int(N) >= 1:
        X = input()
        if (int(X) <= 39) and (int(X) >= 1):
            A.append(X)
            N = int(N) - 1
        elif int(X) == 0:
            A.append(X)
            N = int(N) - 1
        else:
            print("valor invalido")
            N = int(N)

else:
    X = input()
    A.append(X)

for I in A:
    if (int(I) >= 1) and (int(I) <= 39):
        F = fib(int(I))
        print("fib(%d) = %d calls = %d" % (int(I), x - 1, F))
    elif int(I) == 0:
        print("fib(%d) = %d calls = %d" % (0, 0, 0))
