from ambiente import *

## geração da origem e destino
def setOrigemDestino():
    origemx,origemy,destinox,destinoy = 0,0,0,0

    while recompensa[origemx,origemy] != -100:
        origemx = numpy.random.randint(0,36)
        origemy = numpy.random.randint(0,18)

        recompensa[origemx][origemy] = 100

    while recompensa[destinox,destinoy] != -100 and (destinox != origemx and destinoy != origemy):
        destinox = numpy.random.randint(0,36)
        destinoy = numpy.random.randint(0,18)

        recompensa[destinox][destinoy] = 99

        #return origemx,origemy,destinox,destinoy

def setPosicaoInicial():
    posicaox,posicaoy = 0,0

    while recompensa[posicaox,posicaoy] != -100:
        posicaox = numpy.random.randint(0,36)
        posicaoy = numpy.random.randint(0,18)
    return posicaox,posicaoy

def proximoEstado(linhaAtual,colunaAtual,acao):
    proxLinha = 0
    proxColuna = 0

    if acao == 'esquerda':
        return proxLinha,proxColuna-1
    elif acao == 'direita':
        return proxLinha,proxColuna+1
    elif acao == 'cima':
        return proxLinha-1,proxColuna
    elif acao == 'baixo':
        return proxLinha+1,proxColuna

