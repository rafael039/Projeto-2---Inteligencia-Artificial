from funcoes import *

#paramentros de treinamento
epsilon = 0.2
fator_desconto = 0.9
taxa_aprendizado = 0.9

j=1

for tentativa in range(5):
    #redefine valores de recompensa
    #recompensa[5][7] = 100
    #recompensa[13][25] = 99

    linha, coluna = setPosicaoInicial()

    while not isEstadoFinal(linha,coluna):
        linhaAntiga, colunaAntiga = linha, coluna

        linha, coluna,acaoAtual = proximoEstado(linha, coluna, epsilon)
        
        rec = recompensa[linha, coluna]
        qValueAntigo = qsa[linhaAntiga,colunaAntiga,acaoAtual]
        diferenca_temporal = rec + (fator_desconto * np.max(qsa[linha,coluna])) - qValueAntigo

        qValueNovo = qValueAntigo + (taxa_aprendizado * diferenca_temporal)
        qsa[linhaAntiga,colunaAntiga,acaoAtual] = qValueNovo

        print("Tr: "+str(j)+'| x= '+str(linha)+' y= '+str(coluna)+'| Acao:'+acoes[acaoAtual]+'| R: '+str(recompensa[linha][coluna]))

    j+=1
   

print('O desgracadinho ta monstro!')
print("-----------------------------------------------------")
print("-----------------------------------------------------")
print("-----------------------------------------------------")