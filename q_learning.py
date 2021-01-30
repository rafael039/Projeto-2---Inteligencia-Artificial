from funcoes import *

# paramentros de treinamento
# declarados globalmente para manipulação no frontend
epsilon = 0.1
fator_desconto = 0.9
taxa_aprendizado = 0.9
treinamentos = 350000
passos = 350
tentativa = 0
passoAtual = 0

def treinarPonto(linhaDestino,colunaDestino,janela,barraProgresso):
    
    
    recompensa[linhaDestino][colunaDestino] = recompensaDestino

    # este valor deve ser o comprimento da progressbar
    progresso=int(treinamentos/passos) 
    print('Treinando para o ponto ('+str(linhaDestino)+','+str(colunaDestino)+'):')


    for passoAtual in range(progresso):
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

                # feedback do treinamento:
                
                # detalhado
                # print("Tr: "+str(j)+'| x= '+str(linha)+' y= '+str(coluna)+'| Acao:'+acoes[acaoAtual]+'| R: '+str(recompensa[linha][coluna]))

            # simples
            #print(str(j)+' de '+str(treinamentos)+'...')

        #resumido (adicionar for para regular passos)
        print('Treinando ponto: ('+str(linhaDestino)+','+str(colunaDestino)+') - '+str(passoAtual*passos)+' de '+str(treinamentos)+'...')
        #frontEnd
        barraProgresso['value'] = passoAtual*0.1 # aumenta a fluidez da barra de progresso
        print('Passo atual'+str(passoAtual))
        janela.update_idletasks()
        passoAtual+=1
    

    print('O desgracadinho ta monstro!')
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    return qsa