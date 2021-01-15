import numpy as np

linhasAmbiente = 11
colunasAmbiente = 35

temPassageiro = False

acoes = ['cima','baixo','esquerda','direita']

## geração da tabela qsa

qsa = np.full((linhasAmbiente,colunasAmbiente,len(acoes)),0)

## geração da recompensa
i = 0
recompensa = np.full((linhasAmbiente, colunasAmbiente),-100)

#linha 2
for i in range(1,34):
    recompensa[1][i] = -1
#linha 4
for i in range(1,34):
    recompensa[3][i] = -1
#linha 8
for i in range(1,34):
    recompensa[7][i] = -1
#linha 10
for i in range(1,34):
    recompensa[9][i] = -1

#coluna 2
for i in range(1,10):
    recompensa[i][1] = -1

#coluna 10
for i in range (3,8):
    recompensa[i][9] = -1

#coluna 18
for i in range(1,5):
    recompensa[i][17] = -1
for i in range(6,10):
    recompensa[i][17] = -1

#coluna 26
for i in range (3,8):
    recompensa[i][25] = -1

# coluna 35
for i in range(1,10):
    recompensa[i][34] = -1

# definir origem e destino temporariamente
recompensa[5][25] = 100
#recompensa[13][25] = 99

print(recompensa)