from ambiente import *

## geração da origem e destino
def isDestino(linha,coluna):
    if recompensa[linha][coluna] == 99:
        return True
    else :
        return False

def isOrigem(linha,coluna):
    if recompensa[linha][coluna] == 100:
        return True
    else :
        return False

def isParede(linha,coluna):
    if recompensa[linha][coluna] == -100:
        return True
    else: 
        return False



def setOrigemDestino():
    origemx,origemy,destinox,destinoy = 0,0,0,0

    while not isParede(origemx,origemy):
        origemx = np.random.randint(linhasAmbiente)
        origemy = np.random.randint(colunasAmbiente)

        recompensa[origemx][origemy] = 100

    while not isParede(destinox,destinoy) and (destinox != origemx and destinoy != origemy):
        destinox = np.random.randint(linhasAmbiente)
        destinoy = np.random.randint(colunasAmbiente)

        recompensa[destinox][destinoy] = 99

        #return origemx,origemy,destinox,destinoy

def setPosicaoInicial():
    posicaox,posicaoy = 0,0

    while not isParede(posicaox,posicaoy):
        posicaox = np.random.randint(linhasAmbiente)
        posicaoy = np.random.randint(colunasAmbiente)
    return posicaox,posicaoy

def proximaAcao(linhaAtual,colunaAtual,epsilon):
    if np.random.random() < epsilon:
        return np.argmax(qsa[linhaAtual,colunaAtual])
    else:
        return np.random.randint(4)

def proximoEstado(linhaAtual,colunaAtual,acao):
    proxLinha, proxColuna = linhaAtual, colunaAtual

    if acoes[acao] == 'esquerda' and colunaAtual > 0:
        proxColuna -=1
    elif acoes[acao] == 'direita' and colunaAtual < colunasAmbiente -1:
        proxColuna +=1
    elif acoes[acao] == 'cima' and linhaAtual > 0:
        proxLinha -=1
    elif acoes[acao] == 'baixo' and linhaAtual < linhasAmbiente -1:
        proxLinha +=1
    
    return proxLinha,proxColuna

def menorCaminho(linhaInicial,colunaInicial):
    linhaAtual, colunaAtual = linhaInicial, colunaInicial
    caminho = []
    caminho.append([linhaAtual,colunaAtual])

    while not isOrigem(linhaAtual,colunaAtual):
        acao = proximaAcao(linhaAtual,colunaAtual,1)
        linhaAtual,colunaAtual = proximoEstado(linhaAtual,colunaAtual,acao)
        caminho.append([linhaAtual,colunaAtual])
    
    # chegou na origem, redefinindo recompensa
    recompensa[linhaAtual,colunaAtual] = -1 

    while not isDestino(linhaAtual,colunaAtual):
        acao = proximaAcao(linhaAtual,colunaAtual,1)
        linhaAtual,colunaAtual = proximoEstado(linhaAtual,colunaAtual,acao)
        caminho.append([linhaAtual,colunaAtual])
    
