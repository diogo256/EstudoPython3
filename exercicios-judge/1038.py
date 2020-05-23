tabela = ([1, 4.00], [2, 4.50], [3, 5.00], [4, 2.00], [5, 1.50])

cod, quant = input().split()
valorPedido = 0.0

for lista in tabela:
    if int(cod) == lista[0]:
        valorPedido = float(lista[1])

pedido = valorPedido*float(quant)

print("Total: R$ %.2f" % pedido)