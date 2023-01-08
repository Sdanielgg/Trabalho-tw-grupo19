#Bibliotecas
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk       
from PIL import ImageTk,Image 
from gerirJogos import *
from consultar import *

def containerGerirJogos():
    panelJogos = PanedWindow(window,width = 750,height= 450)
    panelJogos.place(x=250, y=50)

    lblJogo = Label(panelJogos,text="Jogo")
    lblJogo.place(x=30,y=70)

    jogo = StringVar()
    entryJogo = Entry(panelJogos,width=25,textvariable=jogo)
    entryJogo.place(x=80,y=70)

    lblCategoria = Label(panelJogos,text="Categoria")
    lblCategoria.place(x=30,y=120)

    categoria =  StringVar()
    listaCategorias = ["FPS","RPG","Battle Royale","Ação-Aventura","Estratégia","Desporto","Corrida","Simulação"]
    cbCategoria = Combobox(panelJogos,values=listaCategorias,textvariable=categoria,width=20)
    cbCategoria.place(x=90,y=120)

    lblPontuacao = Label(panelJogos,text="Pontuação")
    lblPontuacao.place(x=30,y=170)

    pontuacao = StringVar()
    spinPontuacao = Spinbox(panelJogos,width=21,from_=1,to=5,textvariable=pontuacao)
    spinPontuacao.place(x=95,y=170)

    lblAno = Label(panelJogos,text="Ano")
    lblAno.place(x=30,y=220)

    ano = StringVar()
    entryAno = Entry(panelJogos,width=25,textvariable=ano)
    entryAno.place(x=80,y=220)

    tview = ttk.Treeview(panelJogos,height=10,selectmode="browse",columns=("Jogo","Categoria","Pontuação","Ano"),show="headings")

    tview.column("Jogo",width=135,anchor="c")
    tview.column("Categoria",width=100,anchor="c")
    tview.column("Pontuação",width=100,anchor="c")
    tview.column("Ano",width=100,anchor="c")
    tview.heading("Jogo",text="Jogo")
    tview.heading("Categoria",text="Categoria")
    tview.heading("Pontuação",text="Pontuação")
    tview.heading("Ano",text="Ano")
    tview.place(x=280,y=70)

    listaJogos = lerJogos()
    refreshListboxJogos(listaJogos,tview)

    global imageInserir, imageRemover
    imageInserir = PhotoImage(file = "images\\adicionar.png")
    btnInserir = Button(panelJogos, image = imageInserir, width=200, height=48, text = "Inserir Jogo", compound=LEFT,
                command= lambda: inserirJogo(jogo.get(), categoria.get(), pontuacao.get(), ano.get(), tview))
    btnInserir.place(x=280, y= 320)
    
    imageRemover = PhotoImage(file = "images\\remover.png")
    btnRemover = Button(panelJogos, image = imageRemover, width=200, height=48,  text = "Remover Jogo", compound=LEFT,
                command= lambda: removerJogo(tview))
    btnRemover.place(x=510, y= 320)

def containerConsultarJogos():
    panelConsulta = PanedWindow(window,width=750,height=450)
    panelConsulta.place(x=250,y=50)

    lblCategoria = Label(panelConsulta,text="Categoria")
    lblCategoria.place(x=10,y=30)

    categoria =  StringVar()
    listaCategorias = ["FPS","RPG","Battle Royale","Ação-Aventura","Estratégia","Desporto","Corrida","Simulação"]
    cbCategoria = Combobox(panelConsulta,values=listaCategorias,textvariable=categoria,width=20)
    cbCategoria.place(x=70,y=30)

    global imagePesquisa
    imagePesquisa = PhotoImage(file="images\\pesquisar.png")
    btnPesquisar = Button(panelConsulta, width=48, height=48, image = imagePesquisa, command = lambda: filtrarJogos(tview2,categoria.get()))
    btnPesquisar.place(x=250,y=20)

    tview2 = ttk.Treeview(panelConsulta, columns = ("Jogo", "Categoria", "Pontuação", "Ano"), show = "headings", height = 12, selectmode = "browse")
    tview2.column("Jogo", width = 220, anchor = "c")
    tview2.column("Categoria", width = 100, anchor = "c")
    tview2.column("Pontuação", width = 220, anchor = "c")
    tview2.column("Ano", width = 220, anchor = "c")

    tview2.heading("Jogo", text = "Jogo")
    tview2.heading("Categoria", text = "Categoria")
    tview2.heading("Pontuação", text = "Pontuação")
    tview2.heading("Ano", text = "Ano")
    tview2.place(x=20, y=90)

#Main
window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1000                             
appHeight = 500 
x = (screenWidth/2) - (appWidth/2)     
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('Catálogo')

panelOpçoes = PanedWindow(window, bg = "gray", width=250, height=500)
panelOpçoes.place(x=0, y=0)

imageGerir = PhotoImage(file = "images\\gerir.png")
btnOpcaoGerir = Button(panelOpçoes, text = "Gerir \nJogos", image = imageGerir, compound=LEFT, relief = "sunken", 
                    width = 230, height = 68, font="calibri, 11",
                    command=containerGerirJogos)
btnOpcaoGerir.place (x=5, y=130)

imageConsulta = PhotoImage(file = "images\\consultar.png" )
btnOpcao2 = Button(panelOpçoes, text = "Consultar \nJogos", relief = "sunken", image = imageConsulta, compound=LEFT,
                width = 230, height = 68,  font="calibri, 11",
                command= containerConsultarJogos)
btnOpcao2.place (x=5, y=210)

window.mainloop()