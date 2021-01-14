from funcoes import *

#paramentros de treinamento
epsilon = 0.5
fator_desconto = 0.9
taxa_aprendizado = 0.9

for tentativa in range(1000):
    linha, coluna = setPosicaoInicial()

    while not isOrigem(linha,coluna):
        acao = proximaAcao(linha,coluna,epsilon)

        linhaAntiga, colunaAntiga = linha, coluna
        linha, coluna = proximoEstado(linha, coluna, acao)
        
        rec = recompensa[linha, coluna]
        qValueAntigo = qsa[linhaAntiga,colunaAntiga,acao]
        diferenca_temporal = rec + (fator_desconto * np.max(qsa[linha,coluna])) - qValueAntigo

        qValueNovo = qValueAntigo + (taxa_aprendizado * diferenca_temporal)
        qsa[linhaAntiga,colunaAntiga,acao] = qValueNovo

        print("Origem - Atual: "+str(qsa[linha,coluna,acao]))
    
    while not isDestino(linha,coluna):
        acao = proximaAcao(linha,coluna,epsilon)

        linhaAntiga, colunaAntiga = linha, coluna
        linha, coluna = proximoEstado(linha, coluna, acao)
        
        rec = recompensa[linha, coluna]
        qValueAntigo = qsa[linhaAntiga,colunaAntiga,acao]
        diferenca_temporal = rec + (fator_desconto * np.max(qsa[linha,coluna])) - qValueAntigo

        qValueNovo = qValueAntigo + (taxa_aprendizado * diferenca_temporal)
        qsa[linhaAntiga,colunaAntiga,acao] = qValueNovo

        print("Destino - Atual: "+str(qsa[linha,coluna,acao])+"| linha="+str(linha)+" - coluna="+str(coluna))

    i+=1
    print('------------------------------------------')
    print(i)
    print('------------------------------------------')
   

print('O desgracadinho ta monstro!')