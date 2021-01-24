import csv
from funcoes import menorCaminho
from ambiente import *

def transportar(linhaOrigem,colunaOrigem,linhaDestino,colunaDestino):
    
    # definir destino
    recompensa[linhaDestino][colunaDestino] = recompensaDestino
    #print('Carregando arquivo:')

    caminhoArquivo = 'coordenadasTreinadas/ponto ('+str(linhaDestino)+','+str(colunaDestino)+').csv' # caminho do arquivo

    csvArq = open(caminhoArquivo,'r') # ponteiro pra um arquivo
    csvPtr = csv.reader(csvArq,delimiter=',') # ponteiro para um csv

    qsa = [] 
    temp = [] # variável que manipula cada elemento (ações para cada ponto (x,y)) da tabela qsa
    i,j = 0,0

    for row in csvPtr:
        qsa.append(row)
        for csvString in qsa[i]: 
            # removendo caracteres e espaços -> lista de strings
            csvString = csvString.strip('[]')
            temp = csvString.split(' ')

            #remove strings vazias que podem existir em temp, devido a formatação do csv 
            temp = list(filter(None,temp)) 

            # mapeia todos os valores string para int, converte para uma lista e insere na tabela qsa
            qsa[i][j] = list(map(int,temp)) 

            j+=1
            temp=[] 
        i+=1
        j=0

    csvArq.close()

    return menorCaminho(linhaOrigem,colunaOrigem,qsa)