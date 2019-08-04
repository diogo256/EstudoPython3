#https://www.urionlinejudge.com.br/judge/pt/problems/view/1172
X = []

for i in range(10):
    entrada = int(input())

    X.append(entrada)

    if X[i] < 1:
        X[i] = 1

for i in range(10):
    print('X[{}] = {}'.format(i, X[i]))