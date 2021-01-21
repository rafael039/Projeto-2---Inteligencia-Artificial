from q_learning import *

print("Gerando arquivo...")
caminhoArquivo = 'coordenadasTreinadas/ponto ('+str(linhaDestino)+','+str(colunaDestino)+').csv'

csvArq = open(caminhoArquivo,'w')
csvPtr = csv.writer(csvArq,delimiter=',')
for k in qsa: # sendo k, uma linha da tabela qsa, contendo todas as possibilidades para todos os pontos da linha
    csvPtr.writerow(k) 
print("Concluído!")