import tkinter as tk
from tkinter import Label, Toplevel, ttk
from tkinter import messagebox
from backend import *
from q_learning import *

def viajar():
    """
    Função que vai definir a ação do botão viajar 
    """

    origem = comboboxOrigem.get()
    destino = comboboxDestino.get()
    pontosDisponiveis = getPontosTreinados()
    if origem == '' or destino == '':
        messagebox.showerror('Erro','Escolha um ponto!')
        return
    
    if origem not in pontosDisponiveis or destino not in pontosDisponiveis:
        messagebox.showerror('Erro','Ponto inválido!')
        return
        
    print(transportar(origem,destino))


def treinar(linha,coluna):
    """
    Função que vai definir a ação do botão treinar. 
    Recebe um inteiro para a linha e um para a coluna
    """
    # TODO : Print da função treinarPonto() na interface em uma progressBar
    if linha < linhasAmbiente and coluna < colunasAmbiente:
        treinarPonto(linha,coluna)
    else:
        messagebox.showerror('Erro','Este ponto não existe no mapa. \nPor favor, escolha um ponto válido.')
    



def janelaNovoPonto():
    """
    Desenha a janela ao clicar no botão Treinar 
    """
    janNovoPonto=Toplevel(janela)
    janNovoPonto.geometry('250x220')
    janNovoPonto.title('Treinar um novo ponto')

    #
    lblGuiatreinamento = tk.Label(
        master=janNovoPonto,
        text='Use os números de referência \n\
na borda do mapa'
    )
    lblGuiatreinamento.place(x=30,y=5)
    lblLinha = tk.Label(
        master=janNovoPonto,
        text='Linha:'
    )
    lblLinha.place(x=80,y=55)

    entLinha = tk.Entry(
        master=janNovoPonto,
        width=10
    )
    entLinha.place(x=80,y=75)
    #
    lblColuna = tk.Label(
        master=janNovoPonto,
        text='Coluna:'
    )
    lblColuna.place(x=80,y=100)
    
    entColuna = tk.Entry(
        master=janNovoPonto,
        width=10
    )
    entColuna.place(x=80,y=120)
    #
    btnNovoPonto = tk.Button(
        master=janNovoPonto,
        width=7,
        height=1,
        activebackground='#ddd',
        activeforeground='#555',
        text = 'treinar',
        #cria uma função temporária
        command=lambda: treinar(int(entLinha.get()),int(entColuna.get())) 
    )

    btnNovoPonto.place(x=80,y=150)

    #      : Este pedaço do código é da gravação do ponto treinado em disco.
    # TODO : Deve ser inserido em uma nova função do backend,
    #      : que recebe a tabela qsa da função treinarPonto e realiza estes comandos para a gravação

    #######################################################################
    #print('Insira a coordenada do ponto a ser treinado')
    #linhaDestino = int(input('Linha: '))
    #colunaDestino = int(input('Coluna: '))
    #nomePonto = input('Insira o nome desse ponto: ')
    #
    #treinarPonto(linhaDestino,colunaDestino)
    #
    #print("Gerando arquivo...")
    #caminhoArquivo = 'coordenadasTreinadas/'+nomePonto+'.csv'
    #
    #csvArq = open(caminhoArquivo,'w')
    #csvPtr = csv.writer(csvArq,delimiter=',')
    #temp = []
    #temp.append(str(linhaDestino)+' '+str(colunaDestino))
    #csvPtr.writerow(temp)
    #for linhaQsa in qsa: # uma linha da tabela qsa, contém todas as açoes para todos os pontos da linha
    #    csvPtr.writerow(linhaQsa) 
    #print("Concluído!")
    #######################################################################

pontosTreinados = getPontosTreinados()

#declaração das janelas
janela = tk.Tk()
janela.geometry('1280x720')
janela.resizable(width=False,height=False)
janela.title('Taxi')


#declaração das janelas


frameControles = tk.Frame(
    master=janela,
    background='#fed'
)
                          
frameControles.pack_propagate(0)
frameControles.place(width=1280,height=50)

# objetos dentro de frameControles

#

lblListOrigem = tk.Label(
    master=frameControles,
    text='Ponto:'
)
lblListOrigem.place(x=5,y=13)

comboboxOrigem = ttk.Combobox(
    master=frameControles,
    width=10,
    height=5,
    values=pontosTreinados
)
comboboxOrigem.place(x=80,y=13)

#

lblListDestino = tk.Label(
    master=frameControles,
    text='Destino:'
)
lblListDestino.place(x=220,y=13)

comboboxDestino = ttk.Combobox(
    master=frameControles,
    width=10,
    height=5,
    values=pontosTreinados
)
comboboxDestino.place(x=300,y=13)

#

btnTreinarNovoPonto = tk.Button(
    master=frameControles,
    width=5,
    height=1,
    activebackground='#ddd',
    activeforeground='#555',
    text = 'treinar',
    command=janelaNovoPonto
)

btnTreinarNovoPonto.place(x=800,y=8)

#

btnViajar = tk.Button(
    master=frameControles,
    width=5,
    height=1,
    activebackground='#ddd',
    activeforeground='#555',
    text = 'clique',
    command=viajar
)
btnViajar.place(x=1200,y=8)

# fim dos objetos dentro de frameControles

janela.mainloop()

