from q_learning import *

print("Gerando arquivo...")
caminhoArquivo = 'coordenadasTreinadas/'+nomePonto+'.csv'

csvArq = open(caminhoArquivo,'w')
csvPtr = csv.writer(csvArq,delimiter=',')
# BUG = Não está salvando como deveria
csvPtr.writerow('('+str(linhaDestino)+' '+str(colunaDestino)+')')
for linhaQsa in qsa: # uma linha da tabela qsa, contém todas as açoes para todos os pontos da linha
    csvPtr.writerow(linhaQsa) 
print("Concluído!")