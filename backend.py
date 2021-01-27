import csv
from funcoes import menorCaminho
from ambiente import *

def transportar(nomePonto,linhaDestino,colunaDestino):
    
    # definir destino
    recompensa[linhaDestino][colunaDestino] = recompensaDestino
    #print('Carregando arquivo:')

    caminhoArquivo = 'coordenadasTreinadas/'+nomePonto+'.csv' # caminho do arquivo

    csvArq = open(caminhoArquivo,'r') # ponteiro pra um arquivo
    csvPtr = csv.reader(csvArq,delimiter=',') # ponteiro para um csv

    qsa = [] 
    i,j = 0,0
    
    temp = next(csvPtr)
    temp = ''.join(temp)
    temp = temp.strip('()')
    temp = temp.split(' ')
    Origem = list(map(int,temp)) 

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

    return menorCaminho(Origem[0],Origem[1],qsa)