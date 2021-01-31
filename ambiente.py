import numpy as np

# variáveis do ambiente
linhasAmbiente = 9
colunasAmbiente = 21

recompensaCaminho = 0
recompensaDestino = 100
valorParede = -1


# acoes disponiveis
acoes = ['cima','baixo','esquerda','direita']

## geração da tabela qsa
global qsa 
qsa = np.full((linhasAmbiente,colunasAmbiente,len(acoes)),0)

## geração da recompensa
i = 0

recompensa = np.full((linhasAmbiente, colunasAmbiente),valorParede)

def desenhaAmbiente():

    #inicializa matriz de recompensas
    recompensa = np.full((linhasAmbiente, colunasAmbiente),valorParede)
    qsa = np.full((linhasAmbiente,colunasAmbiente,len(acoes)),0)
    #linha 1

    for i in range(0,21):
        recompensa[0][i] = recompensaCaminho
    #linha 3
    for i in range(0,21):
        recompensa[2][i] = recompensaCaminho
    #linha 7
    for i in range(0,21):
        recompensa[6][i] = recompensaCaminho
    #linha 9
    for i in range(0,21):
        recompensa[8][i] = recompensaCaminho

    #coluna 1
    for i in range(0,9):
        recompensa[i][0] = recompensaCaminho

    #coluna 6
    recompensa[3][5] = recompensaCaminho
    recompensa[5][5] = recompensaCaminho

    #coluna 8
    recompensa[1][7] = recompensaCaminho
    recompensa[7][7] = recompensaCaminho

    #coluna 11
    for i in range(2,7):
        recompensa[i][10] = recompensaCaminho

    #coluna 14
    recompensa[1][13] = recompensaCaminho
    recompensa[7][13] = recompensaCaminho

    #coluna 16
    recompensa[3][15] = recompensaCaminho
    recompensa[5][15] = recompensaCaminho

    #coluna 21
    for i in range(0,9):
        recompensa[i][20] = recompensaCaminho

    return recompensa

    # salva a tabela qsa com o mapa
    #arqrec = open('recTable','w')
    #arqrec.write(str(recompensa))