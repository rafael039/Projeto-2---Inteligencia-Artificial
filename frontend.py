import tkinter as tk
from backend import *

def clicado():
    print('clicaram em mim!')

janela = tk.Tk()
janela.geometry('1280x720')
janela.resizable(width=False,height=False)
janela.title('Taxi')

frameControles = tk.Frame(
    master=janela,
    background='#fed'
)
                          
frameControles.pack_propagate(0)
frameControles.place(width=1120,height=50)

# objetos dentro de frameControles

lblListOrigem = tk.Label(
    master=frameControles,
    text='Origem:'
)
lblListOrigem.place(x=5,y=13)


btnViajar = tk.Button(
    master=frameControles,
    width=5,
    height=1,
    activebackground='#ddd',
    activeforeground='#555',
    text = 'clique',
    command=clicado
)
btnViajar.place(x=1000,y=8)


# fim dos objetos dentro de frameControles

janela.mainloop()

#Parte do código a ser integrada:

#linhaOrigem = int(input('Insira a linha de origem: '))
#colunaOrigem = int(input('Insira a coluna de origem: '))
#linhaDest = int(input('Insira a linha de destino: '))
#colunaDest = int(input('Insira a coluna de destino: '))

#print(transportar(linhaOrigem,colunaOrigem,linhaDest,colunaDest))


