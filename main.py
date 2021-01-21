import csv

print('Carregando arquivo:')
#linha = int(input('Insira a linha: '))
#coluna = input('Insira a coluna: '))

linha = 8
coluna = 24


caminhoArquivo = 'coordenadasTreinadas/ponto ('+str(linha)+','+str(coluna)+').csv'

csvArq = open(caminhoArquivo,'r')
csvPtr = csv.reader(csvArq,delimiter=',')

qsaArq = []
i = 0
for row in csvPtr:
    qsaArq.append(row)
    print(qsaArq[i])
    i+=1

# implementar leitura dos arquivos
