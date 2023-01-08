#Bibliotecas
from tkinter import *

def setupPaginaJogo(tview2):
    idJogoSelecionado = tview2.selection()
    items = tview2.item(idJogoSelecionado)
    items = items.get("values")

    return items
    


