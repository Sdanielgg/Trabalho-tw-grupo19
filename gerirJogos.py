#Bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk  

fJogos= "files/jogos.txt"

def inserirJogo(jogo, categoria, pontuacao, ano, tview):
    fileJogos=open(fJogos, "a", encoding="utf-8")
    linha = jogo + ";" + categoria + ";" + pontuacao + ";" + ano + "\n" 
    fileJogos.write(linha)
    fileJogos.close()
    
    lista = lerJogos()
    refreshListboxJogos(lista, tview)

def removerJogo(tview):

    index = tview.index(tview.selection())
    print(index)
    tview.delete(tview.selection())

    fileJogos=open(fJogos, "w+", encoding="utf-8")
    lista = fileJogos.readlines()     
    fileJogos.close()

    lista = lerJogos()
    refreshListboxJogos(lista, tview)


def lerJogos():
    fileJogos=open(fJogos, "r", encoding="utf-8")
    lista = fileJogos.readlines()
    fileJogos.close()
    return lista


def refreshListboxJogos(listaJogos, tview):
    tview.delete(*tview.get_children())
    for item in listaJogos:
        tview.insert("", "end", values = (item.split(";")[0],item.split(";")[1], item.split(";")[2], item.split(";")[3]))