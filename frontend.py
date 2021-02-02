import time
import tkinter as tk
from tkinter import Toplevel, ttk, messagebox
from backend import *
from q_learning import *


def verUltimoCaminho():

    janUltimoCaminho=Toplevel(janela)
    janUltimoCaminho.geometry('300x150')
    janUltimoCaminho.title('Treinar um novo ponto')
    janUltimoCaminho.pack_propagate(0)

    caminho = transportar(origem,destino)

    lblCaminho = tk.Label(
        master=janUltimoCaminho,
        text='O último caminho percorrido foi: [x,y]'
    )
    lblCaminho.place(x=22,y=5)

    strCaminho = ''
    for i in caminho:
        if caminho.index(i) % 5 == 0:
            strCaminho+='\n'
        strCaminho+= str(i)


    lblCaminhoPercorrido = tk.Label(
        master=janUltimoCaminho,
        text=strCaminho
    )
    lblCaminhoPercorrido.place(x=40,y=40)

    


objetosTela = []
origem = ''
destino = ''
def desenharRota(caminho,origem,destino):
    global objetosTela
    # ponto inicial                x0 = 65px | y0 = 50px
    # deslocamento por estado      50 px 
    for i in objetosTela:
        canvasMapa.delete(i)
    coord = []
    deslocamento = 50
    ptInicialX = 65
    ptInicialY = 50
    temp = []
    pontos = []

    ##calculo para desenhar rota

    for i in range (len(caminho)-1):
        inicioReta = caminho[i]
        fimReta = caminho[i+1]
        coord.append(inicioReta[1]*deslocamento+ptInicialX)
        coord.append(inicioReta[0]*deslocamento+ptInicialY)
        coord.append(fimReta[1]*deslocamento+ptInicialX)
        coord.append(fimReta[0]*deslocamento+ptInicialY)

    #calculo para desenhar os pontos
    temp.append(origem[1]*deslocamento+ptInicialX-8)
    temp.append(origem[0]*deslocamento+ptInicialY-8)
    temp.append(origem[1]*deslocamento+ptInicialX+8)
    temp.append(origem[0]*deslocamento+ptInicialY+8)
    pontos.append(temp.copy())
    temp.clear()
    temp.append(destino[1]*deslocamento+ptInicialX-8)
    temp.append(destino[0]*deslocamento+ptInicialY-8)
    temp.append(destino[1]*deslocamento+ptInicialX+8)
    temp.append(destino[0]*deslocamento+ptInicialY+8)
    pontos.append(temp.copy())
    temp.clear()

    objetosTela.append(canvasMapa.create_line(coord,fill='blue',width=3))

    objetosTela.append(canvasMapa.create_oval(pontos[0], fill='red',width=3))
    objetosTela.append(canvasMapa.create_oval(pontos[1], fill='yellow',width=3))

    btnMostrarCaminho['state'] = tk.NORMAL
    
    #print('x= '+str(linhaAtual)+' y= '+str(colunaAtual)+'| Acao:'+acoes[acaoAtual])


def viajar():
    """
    Função que vai definir a ação do botão viajar 
    """
    global origem,destino
    origem = comboboxOrigem.get()
    destino = comboboxDestino.get()
    pontosDisponiveis = getPontosTreinados()
    if origem == '' or destino == '':
        messagebox.showerror('Erro','Escolha um ponto!')
        return
    if origem == destino:
        messagebox.showerror('Erro','A origem é igual ao destino!')
        return

    if origem not in pontosDisponiveis or destino not in pontosDisponiveis:
        messagebox.showerror('Erro','Ponto inválido!')
        return
        
    caminho = transportar(origem,destino)

    # parte gráfica

    desenharRota(caminho,nomeToCoordenada(origem),nomeToCoordenada(destino))

    #canvasCarro = tk.Canvas(width=48,height=48)  # Tamanho da Imagen (48x48 px)
    
    #imagemCarro = tk.PhotoImage(file=os.path.normpath("imagens/CarroPequeno1.png"))
    # X = Muda a posição da Linha -- Posição Inicial (0/) = 40  F = (N_coluna * 50) + PosicaoInicial
    # Y = Muda posição de Coluna  -- Posição Inicial (/0) = 76  F = (N_linha * 50) + PosicaoInicial
    # Passo para avança 50 em 50
    
    #canvasMapa.create_oval(50, 50, 0,0)
    #canvasMapa.update_idletasks()

def treinar(entLinha,entColuna,entNome,janTreinamento,botao):
    """
    Função que manipula a janela dispara o treinamento do ponto. \n
    Argumentos: \n 
    entLinha -- entrada de texto do tkinter para a linha\n
    entColuna -- entrada de texto tkinter para a coluna\n
    entNome -- entrada de texto tkinter para o nome do ponto\n
    janTreinamento -- janela popup do treinamento\n
    botao -- Botão 'Treinar'
    """

    botao['state'] = tk.DISABLED #desabilita botão
    try :
        linha = int(entLinha.get())
        coluna = int(entColuna.get())
        nome = entNome.get()

        #reseta os valores
        
        recompensa = desenhaAmbiente() 

        if linha < linhasAmbiente and coluna < colunasAmbiente:

            lblTreinamento = tk.Label(
                master=janTreinamento,
                text='Treinando...'
            )
            lblTreinamento.place(x=85,y=220)

            progressoTreinamento = ttk.Progressbar(
                janTreinamento, 
                orient='horizontal',
                length=250,
                mode='determinate'
            )
            progressoTreinamento.place(x=5,y=245)

            progressoTreinamento['value'] = 0 #inicializa a barra de progresso
            janela.update_idletasks()
            if not isParede(linha,coluna,recompensa):
                qsa = treinarPonto(linha,coluna,recompensa,janela,progressoTreinamento,lblTreinamento)

                #salvando arquivo
                progressoTreinamento.destroy()
                lblTreinamento['text'] = 'Salvando...'
                janela.update_idletasks()
                time.sleep(1)
                salvarQsa(linha,coluna,nome,qsa)
                lblTreinamento['text'] = 'Concluído!'
                janela.update_idletasks()
                time.sleep(1)
                messagebox.showinfo('Aviso','É necessario reiniciar a aplicação para ver o novo ponto!')
            else:
                messagebox.showerror('Erro','O ponto ('+str(linha)+','+str(coluna)+') é uma parede. \nPor favor, escolha um ponto válido.')
                progressoTreinamento.destroy()
            
            lblTreinamento.destroy()
            
        else:
            messagebox.showerror('Erro','Este ponto não existe no mapa. \nPor favor, escolha um ponto válido.')
    except ValueError:
        messagebox.showerror('Erro!','Linha e coluna inválidos!')
    finally:
        #limpando alterações para um novo treinamento
        entLinha.delete(0,tk.END)
        entColuna.delete(0,tk.END)
        entNome.delete(0,tk.END)
        botao['state'] = tk.NORMAL
        


def janelaNovoPonto():
    """
    Desenha a janela ao clicar no botão Treinar 
    """
    janNovoPonto=Toplevel(janela)
    janNovoPonto.geometry('260x270')
    janNovoPonto.title('Treinar um novo ponto')
    janNovoPonto.pack_propagate(0)

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
    lblNome = tk.Label(
        master=janNovoPonto,
        text='Nome:'
    )
    lblNome.place(x=20,y=145)

    entNome = tk.Entry(
        master=janNovoPonto,
        width=27
    )
    entNome.place(x=20,y=165)
    #
    btnNovoPonto = tk.Button(
        master=janNovoPonto,
        width=7,
        height=1,
        activebackground='#ddd',
        activeforeground='#555',
        text = 'treinar',
        #cria uma função temporária
        command=lambda: treinar(entLinha,entColuna,entNome,janNovoPonto,btnNovoPonto) 
    )

    btnNovoPonto.place(x=80,y=190)


#declaração das janelas
janela = tk.Tk()
janela.geometry('1120x530')
janela.resizable(width=False,height=False)
janela.title('QueroTaxi')


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
    text='Origem:',
    background='#fed'
)
lblListOrigem.place(x=5,y=13)

comboboxOrigem = ttk.Combobox(
    master=frameControles,
    width=20,
    height=5,
    values=pontosTreinados
)
comboboxOrigem.place(x=70,y=13)

#

lblListDestino = tk.Label(
    master=frameControles,
    text='Destino:',
    background='#fed'
)
lblListDestino.place(x=280,y=13)

comboboxDestino = ttk.Combobox(
    master=frameControles,
    width=20,
    height=5,
    values=pontosTreinados
)
comboboxDestino.place(x=350,y=13)

#

btnMostrarCaminho = tk.Button(
    master=frameControles,
    width=8,
    height=1,
    activebackground='#ddd',
    activeforeground='#555',
    text = 'Ver Caminho',
    command=verUltimoCaminho,
    state=tk.DISABLED
)
btnMostrarCaminho.place(x=550,y=8)

#

btnTreinarNovoPonto = tk.Button(
    master=frameControles,
    width=5,
    height=1,
    activebackground='#ddd',
    activeforeground='#555',
    text = 'Treinar',
    command=janelaNovoPonto
)

btnTreinarNovoPonto.place(x=900,y=8)
#

btnViajar = tk.Button(
    master=frameControles,
    width=5,
    height=1,
    activebackground='#ddd',
    activeforeground='#555',
    text = 'Viajar',
    command=viajar
)
btnViajar.place(x=1000,y=8)

# fim dos objetos dentro de frameControles

# Imagem
canvasMapa = tk.Canvas(master=janela,width=1120,height=480)
canvasMapa.place(x=0,y=51)
imagemMapa = tk.PhotoImage(file=os.path.normpath("imagens/Cenario.png")) 
canvasMapa.create_image(0, 0, image=imagemMapa, anchor='nw')

janela.mainloop()
