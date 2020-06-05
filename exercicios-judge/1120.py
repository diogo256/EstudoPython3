def remover(arg1, arg2):
    ret = ""
    for c in arg2:
        if c != arg1:
            ret += c
    if ret == "" or int(ret) == 0:
        ret = 0
    return int(ret)

D, N = map(int, input().split())

while (D > 0 and N > 0) and D <=9 and N <= 10**100:
    valor = remover(str(D),str(N))
    print(valor)
    D, N = map(int, input().split())