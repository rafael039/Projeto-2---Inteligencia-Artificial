from backend import *

linhaOrigem = int(input('Insira a linha de origem: '))
colunaOrigem = int(input('Insira a coluna de origem: '))
linhaDest = int(input('Insira a linha de destino: '))
colunaDest = int(input('Insira a coluna de destino: '))

print(transportar(linhaOrigem,colunaOrigem,linhaDest,colunaDest))


