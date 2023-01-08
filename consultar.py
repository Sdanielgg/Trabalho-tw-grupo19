#Bibliotecas
from tkinter import *
from gerirJogos import refreshListboxJogos

fJogos= "files/jogos.txt"

def filtrarJogos(tview2,categoria):
    tview2.delete(*tview2.get_children())

    fileJogos=open(fJogos, "r", encoding="utf-8")
    lista = fileJogos.readlines()
    fileJogos.close()
    
    if categoria == "Todas":
        refreshListboxJogos(lista,tview2)
    else:
        for line in lista:
            if line == "": continue
            campos = line.split(";")
            if campos[1] == categoria:
                tview2.insert("", "end", values = (line.split(";")[0],line.split(";")[1], line.split(";")[2], line.split(";")[3] ))