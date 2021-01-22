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
temp = []
i,j = 0,0

for row in csvPtr:
    qsaArq.append(row)
    # traduz elementos string em int
    for csvString in qsaArq[i]: 
        # removendo caracteres e espaços -> lista de strings
        csvString = csvString.strip('[]')
        temp = csvString.split(' ')

        ##### BUG: Não consegue remover todas as strings vazias
        csvString = list(filter(None,csvString)) # remove itens vazios, inseridos devido a formatação do csv
        ##### TODO: Remover strings vazias para fazer a conversão para int

        # mapeia todos os valores string para int, converte para uma lista e insere na tabela qsa
        qsaArq[i][j] = list(map(int,temp)) 
        j+=1
        temp=[]
    i+=1


temp.append(int(qsaArq[0][0][1]))
temp.append(int(qsaArq[0][0][3]))
temp.append(int(qsaArq[0][0][5]))
temp.append(int(qsaArq[0][0][7]))

qsaArq[0][0] = temp

print(qsaArq[0][0])
# implementar leitura dos arquivos
