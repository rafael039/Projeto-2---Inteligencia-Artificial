from funcoes import *

#paramentros de treinamento
epsilon = 0.2
fator_desconto = 0.9
taxa_aprendizado = 0.9
treinamentos = 10000

j=1

print('Treinando para o ponto ('+str(linhaDestino)+','+str(colunaDestino)+'):')

for tentativa in range(treinamentos):

    linha, coluna = setPosicaoInicial()

    while not isEstadoFinal(linha,coluna):
        linhaAntiga, colunaAntiga = linha, coluna

        linha, coluna,acaoAtual = proximoEstado(linha, coluna, epsilon)
        
        rec = recompensa[linha, coluna]
        qValueAntigo = qsa[linhaAntiga,colunaAntiga,acaoAtual]
        diferenca_temporal = rec + (fator_desconto * np.max(qsa[linha,coluna])) - qValueAntigo

        qValueNovo = qValueAntigo + (taxa_aprendizado * diferenca_temporal)
        qsa[linhaAntiga,colunaAntiga,acaoAtual] = qValueNovo

        # escolha o feedback do treinamento:
        
        # detalhado
        # print("Tr: "+str(j)+'| x= '+str(linha)+' y= '+str(coluna)+'| Acao:'+acoes[acaoAtual]+'| R: '+str(recompensa[linha][coluna]))

    # simples
    print(str(j)+' de '+str(treinamentos)+'...')

    j+=1
   

print('O desgracadinho ta monstro!')
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")