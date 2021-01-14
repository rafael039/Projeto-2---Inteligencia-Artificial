import numpy as np

linhasAmbiente = 19
colunasAmbiente = 37

temPassageiro = False

acoes = ['cima','baixo','esquerda','direita']

## geração da tabela qsa

qsa = np.full((linhasAmbiente,colunasAmbiente,len(acoes)),0)

## geração da recompensa
i = 0
recompensa = np.full((linhasAmbiente, colunasAmbiente),-100)

#linha 2
for i in range(1,36):
    recompensa[1][i] = -1
#linha 6
for i in range(1,36):
    recompensa[5][i] = -1
#linha 14
for i in range(1,36):
    recompensa[13][i] = -1
#linha 18
for i in range(1,36):
    recompensa[17][i] = -1

#coluna 2
for i in range(1,19):
    recompensa[i][1] = -1

#coluna 19
for i in range(1,10):
    recompensa[i][18] = -1
for i in range(11,18):
    recompensa[i][18] = -1

# coluna 36
for i in range(1,19):
    recompensa[i][35] = -1

# definir origem e destino temporariamente
recompensa[5][7] = 100
recompensa[13][25] = 99