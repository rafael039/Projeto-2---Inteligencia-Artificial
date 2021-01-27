from funcoes import *

print('Insira a coordenada do ponto a ser treinado')
linhaDestino = int(input('Linha: '))
colunaDestino = int(input('Coluna: '))
nomePonto = input('Insira o nome desse ponto: ')

recompensa[linhaDestino][colunaDestino] = recompensaDestino

#paramentros de treinamento
epsilon = 0.1
fator_desconto = 0.9
taxa_aprendizado = 0.9
treinamentos = 350000
passos = 10
j=1
k=int(treinamentos/passos)
print('Treinando para o ponto ('+str(linhaDestino)+','+str(colunaDestino)+'):')


for passo in range(k):
    for tentativa in range(passos):

        linha, coluna = setPosicaoInicial()

        while not isEstadoFinal(linha,coluna):
            linhaAntiga, colunaAntiga = linha, coluna

            linha, coluna,acaoAtual = proximoEstado(linha, coluna, epsilon,qsa)
            
            rec = recompensa[linha, coluna]
            qValueAntigo = qsa[linhaAntiga,colunaAntiga,acaoAtual]
            diferenca_temporal = rec + (fator_desconto * np.max(qsa[linha,coluna])) - qValueAntigo

            qValueNovo = qValueAntigo + (taxa_aprendizado * diferenca_temporal)
            qsa[linhaAntiga,colunaAntiga,acaoAtual] = qValueNovo

            # escolha o feedback do treinamento:
            
            # detalhado
            # print("Tr: "+str(j)+'| x= '+str(linha)+' y= '+str(coluna)+'| Acao:'+acoes[acaoAtual]+'| R: '+str(recompensa[linha][coluna]))

        # simples
        #print(str(j)+' de '+str(treinamentos)+'...')

    #resumido (adicionar for para regular passos)
    print('Treinando ponto: ('+str(linhaDestino)+','+str(colunaDestino)+') - '+str(j*passos)+' de '+str(treinamentos)+'...')

    j+=1
   

print('O desgracadinho ta monstro!')
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")