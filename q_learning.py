from funcoes import *

#paramentros de treinamento
epsilon = 0.2
fator_desconto = 0.9
taxa_aprendizado = 0.9

j=1

for tentativa in range(1000):
    #redefine valores de recompensa
    #recompensa[5][7] = 100
    #recompensa[13][25] = 99

    linha, coluna = setPosicaoInicial()

    while not isEstadoFinal(linha,coluna):
        acao = proximaAcao(linha,coluna,epsilon)

        linhaAntiga, colunaAntiga = linha, coluna
        linha, coluna = proximoEstado(linha, coluna, acao)
        
        rec = recompensa[linha, coluna]
        qValueAntigo = qsa[linhaAntiga,colunaAntiga,acao]
        diferenca_temporal = rec + (fator_desconto * np.max(qsa[linha,coluna])) - qValueAntigo

        qValueNovo = qValueAntigo + (taxa_aprendizado * diferenca_temporal)
        qsa[linhaAntiga,colunaAntiga,acao] = qValueNovo

        print("Tr: "+str(j)+'| x= '+str(linha)+' y= '+str(coluna)+'| Acao:'+acoes[acao])

    j+=1
   

print('O desgracadinho ta monstro!')