from funcoes import *

# paramentros de treinamento
# declarados globalmente para manipulação no frontend
epsilon = 0.2
fator_desconto = 0.92
taxa_aprendizado = 0.9
treinamentos = 5000
passos = 5
tentativa = 0
passoAtual = 0

def treinarPonto(linhaDestino,colunaDestino,recompensa,janela,barraProgresso,label):
    recompensa[linhaDestino][colunaDestino] = recompensaDestino

    # este valor deve ser o comprimento da progressbar
    progresso=int(treinamentos/passos) 
    #print('Treinando para o ponto ('+str(linhaDestino)+','+str(colunaDestino)+'):')


    for passoAtual in range(progresso):
        for tentativa in range(passos):

            linha, coluna = setPosicaoInicial(recompensa)

            while not isEstadoFinal(linha,coluna,recompensa):
                linhaAntiga, colunaAntiga = linha, coluna

                linha, coluna,acaoAtual = proximoEstado(linha, coluna, epsilon,qsa,recompensa)
                
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
        #print('Treinando ponto: ('+str(linhaDestino)+','+str(colunaDestino)+') - '+str(passoAtual*passos)+' de '+str(treinamentos)+'...')
        #frontEnd
        barraProgresso['value'] = passoAtual/10 # aumenta a fluidez da barra de progresso
        label['text'] = 'Treinando... '+str(passoAtual/10)+'%'
        #print('Passo atual'+str(passoAtual))
        janela.update_idletasks()
        passoAtual+=1
    

    #print('O desgracadinho ta monstro!')
    #print("-----------------------------------------------------")
    #print("-----------------------------------------------------")
    #print("-----------------------------------------------------")
    return qsa