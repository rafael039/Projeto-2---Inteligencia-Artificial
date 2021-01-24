from backend import *

linhaOrigem = int(input('Insira a linha de origem: '))
colunaOrigem = int(input('Insira a coluna de origem: '))
linhaDestino = int(input('Insira a linha de destino: '))
colunaDestino = int(input('Insira a coluna de destino: '))

print(transportar(linhaOrigem,colunaOrigem,linhaDestino,colunaDestino))


