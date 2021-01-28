import os
import csv
from funcoes import menorCaminho
from ambiente import *

def transportar(pontoOrigem,pontoDestino):

    qsa = [] 
    i,j = 0,0

    caminhoArquivo = 'coordenadasTreinadas/'+pontoDestino+'.csv' # caminho do arquivo

    csvArq = open(caminhoArquivo,'r') # ponteiro pra um arquivo
    csvPtr = csv.reader(csvArq,delimiter=',') # ponteiro para um csv
    
    # definir destino
    linhaOrigem,colunaOrigem = nomeToCoordenada(pontoOrigem)
    linhaDestino,colunaDestino = nomeToCoordenada(pontoDestino)
    recompensa[linhaDestino][colunaDestino] = recompensaDestino

    next(csvPtr) # pula a primeira linha

    for row in csvPtr:
        qsa.append(row)
        for csvString in qsa[i]: 
            # removendo caracteres e espaços -> lista de strings
            csvString = csvString.strip('[]')
            csvString = csvString.split(' ')

            #remove strings vazias que podem existir em temp, devido a formatação do csv 
            csvString = list(filter(None,csvString)) 

            # mapeia todos os valores string para int, converte para uma lista e insere na tabela qsa
            qsa[i][j] = list(map(int,csvString)) 

            j+=1
            temp=[] 
        i+=1
        j=0

    csvArq.close()
    
    return menorCaminho(linhaOrigem,colunaOrigem,qsa)

def nomeToCoordenada(pontoTaxi):

    caminhoArquivo = 'coordenadasTreinadas/'+pontoTaxi+'.csv' # caminho do arquivo

    csvArq = open(caminhoArquivo,'r') # ponteiro pra um arquivo
    csvPtr = csv.reader(csvArq,delimiter=',') # ponteiro para um csv

    linhaTemp = next(csvPtr)
    linhaTemp = ''.join(linhaTemp)
    linhaTemp = linhaTemp.split(' ')
    coordenada = list(map(int,linhaTemp)) 

    return coordenada

# retorna o nome dos pontos treinados que estão na pasta coordenadastreinadas
def getPontosTreinados():
    
    i=0
    pontosTreinados = os.listdir('coordenadasTreinadas')
    for ponto in pontosTreinados:
        if ponto.startswith('.'):
            pontosTreinados.remove(ponto)
        else:
            ponto = ponto.split('.csv')
            pontosTreinados[i] = ponto[0]
        i+=1
    return pontosTreinados


