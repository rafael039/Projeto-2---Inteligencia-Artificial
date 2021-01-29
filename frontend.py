import tkinter as tk
from tkinter import Toplevel, ttk, messagebox
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


def treinar(linha,coluna,nome):
    """
    Função que vai definir a ação do botão treinar. 
    Recebe um inteiro para a linha e um para a coluna
    """
    # TODO : Print da função treinarPonto() na interface em uma progressBar
    if linha < linhasAmbiente and coluna < colunasAmbiente:
        treinarPonto(linha,coluna)
        print("Gerando arquivo...")
        salvarQsa(linha,coluna,nome,qsa)
    else:
        messagebox.showerror('Erro','Este ponto não existe no mapa. \nPor favor, escolha um ponto válido.')
    



def janelaNovoPonto():
    """
    Desenha a janela ao clicar no botão Treinar 
    """
    janNovoPonto=Toplevel(janela)
    janNovoPonto.geometry('250x270')
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
    lblNome = tk.Label(
        master=janNovoPonto,
        text='Nome:'
    )
    lblNome.place(x=80,y=140)

    entNome = tk.Entry(
        master=janNovoPonto,
        width=10
    )
    entNome.place(x=80,y=160)
    #
    btnNovoPonto = tk.Button(
        master=janNovoPonto,
        width=7,
        height=1,
        activebackground='#ddd',
        activeforeground='#555',
        text = 'treinar',
        #cria uma função temporária
        command=lambda: treinar(int(entLinha.get()),int(entColuna.get()),entNome.get()) 
    )

    btnNovoPonto.place(x=80,y=190)


pontosTreinados = getPontosTreinados()

#declaração das janelas
janela = tk.Tk()
janela.geometry('1120x530')
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
canvasMapa = tk.Canvas(width=1120,height=480)
canvasMapa.place(x=0,y=51)
imagemMapa = tk.PhotoImage(file="imagens/Cenario.png") 
canvasMapa.create_image(0, 0, image=imagemMapa, anchor='nw')

janela.mainloop()

