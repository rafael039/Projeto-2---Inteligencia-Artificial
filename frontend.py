import tkinter as tk
from tkinter import ttk
from backend import *

def clicado():
    print(transportar(comboboxOrigem.get(),comboboxDestino.get()))

pontosTreinados = getPontosTreinados()

janela = tk.Tk()
janela.geometry('1280x720')
janela.resizable(width=False,height=False)
janela.title('Taxi')

frameControles = tk.Frame(
    master=janela,
    background='#fed'
)
                          
frameControles.pack_propagate(0)
frameControles.place(width=1280,height=50)

# objetos dentro de frameControles

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


btnViajar = tk.Button(
    master=frameControles,
    width=5,
    height=1,
    activebackground='#ddd',
    activeforeground='#555',
    text = 'clique',
    command=clicado
)
btnViajar.place(x=1200,y=8)

# fim dos objetos dentro de frameControles

janela.mainloop()

#Parte do código a ser integrada:

#nomeOrigem = input('insira o nome do ponto de taxi de origem: ')
#nomeDestino = input('insira o nome do ponto de taxi de origem')


#print(transportar(nomeOrigem,nomeDestino))


