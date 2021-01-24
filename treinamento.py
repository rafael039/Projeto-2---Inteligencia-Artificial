from q_learning import *

print("Gerando arquivo...")
caminhoArquivo = 'coordenadasTreinadas/ponto ('+str(linhaDestino)+','+str(colunaDestino)+').csv'

csvArq = open(caminhoArquivo,'w')
csvPtr = csv.writer(csvArq,delimiter=',')
for linhaQsa in qsa: # uma linha da tabela qsa, contém todas as açoes para todos os pontos da linha
    csvPtr.writerow(linhaQsa) 
print("Concluído!")