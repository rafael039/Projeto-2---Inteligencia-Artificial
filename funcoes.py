from ambiente import *

## geração da origem e destino
def isEstadoFinal(linha,coluna,recompensa):
    if recompensa[linha][coluna] == recompensaDestino:
        return True
    else :
        return False

def isParede(linha,coluna,recompensa):
    if recompensa[linha][coluna] == valorParede:
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

def setPosicaoInicial(recompensa):
    posicaox,posicaoy = 0,0

    posicaox = np.random.randint(linhasAmbiente)
    posicaoy = np.random.randint(colunasAmbiente)

    while isParede(posicaox,posicaoy,recompensa):
        posicaox = np.random.randint(linhasAmbiente)
        posicaoy = np.random.randint(colunasAmbiente)
    return posicaox,posicaoy

def proximaAcao(linhaAtual,colunaAtual,epsilon,qsa):
    if np.random.random() <= epsilon:
        return np.argmax(qsa[linhaAtual][colunaAtual])
    else:
        return np.random.randint(4)
        # enquanto o próximo estado der numa parede, peça um novo estado

def proximaAcaoAleatoria(acoes):
        return np.random.choice(acoes)
        
def proximoEstado(linhaAtual,colunaAtual,epsilon,qsa,recompensa):
    proxLinha, proxColuna = linhaAtual, colunaAtual
    listaAcoes = acoes.copy()
    iAcao = proximaAcao(linhaAtual,colunaAtual,epsilon,qsa)
    

    if acoes[iAcao] == 'esquerda' and colunaAtual > 0:
        proxColuna -=1
    elif acoes[iAcao] == 'direita' and colunaAtual < colunasAmbiente -1:
        proxColuna +=1
    elif acoes[iAcao] == 'cima' and linhaAtual > 0:
        proxLinha -=1
    elif acoes[iAcao] == 'baixo' and linhaAtual < linhasAmbiente -1:
        proxLinha +=1
    

    while recompensa[proxLinha][proxColuna] == -1 : #úkltima ação deu errado
        listaAcoes.remove(acoes[iAcao]) #remove ação anterior
        acaoStr = proximaAcaoAleatoria(listaAcoes)

        proxLinha, proxColuna = linhaAtual, colunaAtual

        if acaoStr == 'esquerda' and colunaAtual > 0:
            proxColuna -=1
        elif acaoStr == 'direita' and colunaAtual < colunasAmbiente -1:
            proxColuna +=1
        elif acaoStr == 'cima' and linhaAtual > 0:
            proxLinha -=1
        elif acaoStr == 'baixo' and linhaAtual < linhasAmbiente -1:
            proxLinha +=1
        iAcao = acoes.index(acaoStr)

    return proxLinha,proxColuna,iAcao

def menorCaminho(linhaInicial,colunaInicial,qsa,recompensa):
    if isEstadoFinal(linhaInicial,colunaInicial,recompensa):
        return []
    else:
        linhaAtual, colunaAtual = linhaInicial, colunaInicial
        caminho = []
        caminho.append([linhaAtual,colunaAtual])

        while not isEstadoFinal(linhaAtual,colunaAtual,recompensa):

            linhaAtual,colunaAtual,acaoAtual = proximoEstado(linhaAtual,colunaAtual,1,qsa,recompensa)

            caminho.append([linhaAtual,colunaAtual])
            
            print('x= '+str(linhaAtual)+' y= '+str(colunaAtual)+'| Acao:'+acoes[acaoAtual])
            #print(isEstadoFinal(linhaAtual,colunaAtual))
    return caminho

