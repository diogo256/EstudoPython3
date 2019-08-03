
from math import sqrt

p1 = input().split(" ")
p2 = input().split(" ")

DISTANCIA = sqrt( ((float(p2[0]) - float(p1[0])) ** 2) + ((float(p2[1]) - float(p1[1])) ** 2) )

print("%0.4f" % DISTANCIA)