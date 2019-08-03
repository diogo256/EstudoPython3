from itertools import permutations

caracteres = "aba"
for subset in permutations(caracteres, 2):
    print(len(subset))