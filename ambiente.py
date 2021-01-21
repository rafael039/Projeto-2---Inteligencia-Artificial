import numpy as np
import csv

linhasAmbiente = 9
colunasAmbiente = 33

temPassageiro = False

recompensaCaminho = 0
recompensaDestino = 100
valorParede = -1

linhaDestino = 8
colunaDestino = 24

acoes = ['cima','baixo','esquerda','direita']

## geração da tabela qsa

qsa = np.full((linhasAmbiente,colunasAmbiente,len(acoes)),0)

## geração da recompensa
i = 0
recompensa = np.full((linhasAmbiente, colunasAmbiente),valorParede)

#linha 1
for i in range(0,33):
    recompensa[0][i] = recompensaCaminho
#linha 3
for i in range(0,33):
    recompensa[2][i] = recompensaCaminho
#linha 7
for i in range(0,33):
    recompensa[6][i] = recompensaCaminho
#linha 9
for i in range(0,33):
    recompensa[8][i] = recompensaCaminho

#coluna 1
for i in range(0,9):
    recompensa[i][0] = recompensaCaminho

#coluna 9
for i in range (2,7):
    recompensa[i][8] = recompensaCaminho

#coluna 17
for i in range(0,4):
    recompensa[i][16] = recompensaCaminho
for i in range(5,9):
    recompensa[i][16] = recompensaCaminho

#coluna 25
for i in range (2,7):
    recompensa[i][24] = recompensaCaminho

# coluna 34
for i in range(0,9):
    recompensa[i][32] = recompensaCaminho

# definir origem e destino
recompensa[linhaDestino][colunaDestino] = recompensaDestino

#print(recompensa)