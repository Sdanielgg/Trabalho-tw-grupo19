#Bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk       
#from PIL import ImageTk,Image
from gerirJogos import *
from consultar import *
from paginaJogo import *
############################ FUNCTIONS ###############################
#Login
def logInPg():
    login=Toplevel()
    
    # Window placement code
    appWidth = 600
    appHeight = 250

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)

    login.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

    login.title("Login")
    login.resizable(0,0)

        # Label Entry Username
    lbl_username = Label(login, text="Username:", fg="red", font=("TkDefaultFont 11"))
    lbl_username.place(x=150, y=40)

    # Entry Username
    txt_username = Entry(login, width=25)
    txt_username.place(x=250, y=40)

    # Label Entry Password
    lbl_password = Label(login, text="Password:", fg="red", font=("TkDefaultFont 11"))
    lbl_password.place(x=150, y=70)

    # Entry Password
    txt_password = Entry(login, width=25, show="*")
    txt_password.place(x=250, y=70)

    # Button Log in
    btn_login = Button(login, text="Iniciar Sessão", fg="blue", relief="raised", bd=3, width=20, height=2)
    btn_login.place(x=380, y=150)

    login.mainloop()

def signUpPg():
    signup=Toplevel()

    # Window placement code
    screenWidth = signup.winfo_screenwidth()
    screenHeight = signup.winfo_screenheight()

    appWidth = 600
    appHeight = 300

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)

    signup.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

    signup.title("Sign Up")
    signup.resizable(0,0)

    ############################ ELEMENTS ###############################

    # Label Entry Username
    lbl_username = Label(signup, text="Username:", fg="red", font=("TkDefaultFont 11"))
    lbl_username.place(x=170, y=40)

    # Entry Username
    txt_username = Entry(signup, width=25)
    txt_username.place(x=270, y=40)

    # Label Entry Password
    lbl_password = Label(signup, text="Password:", fg="red", font=("TkDefaultFont 11"))
    lbl_password.place(x=170, y=70)

    # Entry Password
    txt_password = Entry(signup, width=25, show="*")
    txt_password.place(x=270, y=70)

    # Label Entry Password
    lbl_passwordConfirm = Label(signup, text="Password Confirmation:", fg="red", font=("TkDefaultFont 11"))
    lbl_passwordConfirm.place(x=85, y=100)

    # Entry Password Confirmation
    txt_passwordConfirm = Entry(signup, width=25, show="*")
    txt_passwordConfirm.place(x=270, y=100)

    # RadioButton Account Type
    selected = StringVar()
    selected.set("user")

    rdbtn_userAcc = Radiobutton(signup, text="Conta User Normal", fg="blue", value="user", variable=selected)
    rdbtn_userAcc.place(x=170, y=160)

    rdbtn_adminAcc = Radiobutton(signup, text="Conta Admin", fg="blue", value="admin", variable=selected)
    rdbtn_adminAcc.place(x=170, y=200)

    # Button Sign up
    btn_signUp = Button(signup, text="Criar Conta", fg="blue", relief="raised", bd=3, width=10, height=5)
    btn_signUp.place(x=350, y=150)

    ############################ MAINLOOP ###############################
    signup.mainloop()
############################ CATALOGO ###############################
def abrirCatalogo():

    def containerGerirJogos():
        panelJogos = PanedWindow(window,width = 750,height= 800)
        panelJogos.place(x=250, y=0)

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
        spinPontuacao = Spinbox(panelJogos,width=3,from_=1,to=5,textvariable=pontuacao)
        spinPontuacao.place(x=95,y=172)

        lblAno = Label(panelJogos,text="Ano")
        lblAno.place(x=30,y=220)

        ano = StringVar()
        entryAno = Entry(panelJogos,width=25,textvariable=ano)
        entryAno.place(x=80,y=220)

        tview = ttk.Treeview(panelJogos,height=10,selectmode="browse",columns=("Jogo","Categoria","Pontuação","Ano"),show="headings")

        scrollb = ttk.Scrollbar(panelJogos,orient="vertical",command=tview.yview)
        scrollb.place(x=718,y=70,height=225)
        tview.configure(yscrollcommand=scrollb.set)
    
        tview.column("Jogo",width=135,anchor="c")
        tview.column("Categoria",width=100,anchor="c")
        tview.column("Pontuação",width=100,anchor="c")
        tview.column("Ano",width=100,anchor="c")
        tview.heading("Jogo",text="Jogo")
        tview.heading("Categoria",text="Categoria")
        tview.heading("Pontuação",text="Pontuação")
        tview.heading("Ano",text="Ano")
        tview.place(x=280,y=70)

        global imageInserir, imageRemover
        imageInserir = PhotoImage(file = "images\\adicionar.png")
        btnInserir = Button(panelJogos, image = imageInserir, width=200, height=48, text = "Inserir Jogo", compound=LEFT,
                    command= lambda: inserirJogo(jogo.get(), categoria.get(), pontuacao.get(), ano.get(), tview))
        btnInserir.place(x=280, y= 320)
        
        imageRemover = PhotoImage(file = "images\\remover.png")
        btnRemover = Button(panelJogos, image = imageRemover, width=200, height=48,  text = "Remover Jogo", compound=LEFT,
                    command= lambda: removerJogo(tview))
        btnRemover.place(x=510, y= 320)
    
        listaJogos = lerJogos()
        refreshListboxJogos(listaJogos,tview)
    
    def containerConsultarJogos():
        panelConsulta = PanedWindow(window,width=750,height=800)
        panelConsulta.place(x=250,y=0)
    
        lblCategoria = Label(panelConsulta,text="Categoria")
        lblCategoria.place(x=10,y=30)
    
        categoria =  StringVar()
        listaCategorias = ["Todas","FPS","RPG","Battle Royale","Ação-Aventura","Estratégia","Desporto","Corrida","Simulação"]
        cbCategoria = Combobox(panelConsulta,values=listaCategorias,textvariable=categoria,width=20)
        cbCategoria.place(x=70,y=30)
    
        global imagePesquisa,imageIrPaginaJogo
        imagePesquisa = PhotoImage(file="images\\pesquisar.png")
        btnPesquisar = Button(panelConsulta, width=48, height=48, image = imagePesquisa, command = lambda: filtrarJogos(tview2,categoria.get()))
        btnPesquisar.place(x=250,y=20)
    
        imageIrPaginaJogo = PhotoImage(file = "images\\ir_pagina_jogo.png")
        btnInserir = Button(panelConsulta, image = imageIrPaginaJogo, width=200, height=48, text = "Página Jogo", compound=LEFT,
                    command= lambda: containerPaginaJogo(tview2))
        btnInserir.place(x=350, y= 20)
    
        tview2 = ttk.Treeview(panelConsulta, columns = ("Jogo", "Categoria", "Pontuação", "Ano"), show = "headings", height = 12, selectmode = "browse")
    
        scrollb = ttk.Scrollbar(panelConsulta,orient="vertical",command=tview2.yview)
        scrollb.place(x=623,y=90,height=265)
        tview2.configure(yscrollcommand=scrollb.set)
    
        tview2.column("Jogo", width = 220, anchor = "c")
        tview2.column("Categoria", width = 180, anchor = "c")
        tview2.column("Pontuação", width = 100, anchor = "c")
        tview2.column("Ano", width = 100, anchor = "c")
    
        tview2.heading("Jogo", text = "Jogo")
        tview2.heading("Categoria", text = "Categoria")
        tview2.heading("Pontuação", text = "Pontuação")
        tview2.heading("Ano", text = "Ano")
        tview2.place(x=20, y=90)

    def containerPaginaJogo(tview2):
    
        items = setupPaginaJogo(tview2)
        panelPaginaJogo = PanedWindow(window,width=750,height=450)
        panelPaginaJogo.place(x=250,y=10)
    
        lblJogo = Label(panelPaginaJogo,text="Jogo",font=("Arial",15),relief="raised")
        lblJogo.place(x=50,y=0)
    
        lblCategoria = Label(panelPaginaJogo,text="Categoria",font=("Arial",15),relief="raised")
        lblCategoria.place(x=50,y=35)
    
        lblPontuacao = Label(panelPaginaJogo,text="Pontuação",font=("Arial",15),relief="raised")
        lblPontuacao.place(x=50,y=70)
    
        lblAno = Label(panelPaginaJogo,text="Ano",font=("Arial",15),relief="raised")
        lblAno.place(x=50,y=105)
    
        jogo = StringVar()
        categoria = StringVar()
        pontuacao = StringVar()
        ano = StringVar()
        jogo.set(items[0])
        categoria.set(items[1])
        pontuacao.set(items[2])
        ano.set(items[3])
    
    
        lblJogo2 = Label(panelPaginaJogo,textvariable=jogo)
        lblJogo2.place(x=100,y=5)
    
        lblCategoria2 = Label(panelPaginaJogo,textvariable=categoria)
        lblCategoria2.place(x=145,y=40)
    
        lblPontuacao2 = Label(panelPaginaJogo,textvariable=pontuacao)
        lblPontuacao2.place(x=150,y=75)
    
        lblAno2 = Label(panelPaginaJogo,textvariable=ano)
        lblAno2.place(x=90,y=110)
    
        global imageAdicionar
        imageAdicionar = PhotoImage(file = "images\\adicionar.png")
        btnAdicionar = Button(panelPaginaJogo, image = imageAdicionar, width=200, height=48, text = "Adicionar aos\nmeus jogos", compound=LEFT)
        btnAdicionar.place(x=500, y= 4)
    
        btnAdicionar2 = Button(panelPaginaJogo, image = imageAdicionar, width=200, height=48, text = "Adicionar aos\nfavoritos", compound=LEFT)
        btnAdicionar2.place(x=500, y= 80)
    
        btnPontuar = Button(panelPaginaJogo,width=10, height=1, text = "Pontuar Jogo")
        btnPontuar.place(x=350, y= 4)
    
        pontuacao2 = StringVar()
        spinPontuacao = Spinbox(panelPaginaJogo,width=3,from_=1,to=5,textvariable=pontuacao2)
        spinPontuacao.place(x=440,y=7)
    
        tview3 = ttk.Treeview(panelPaginaJogo, columns = ("Utilizador", "Comentário"), show = "headings", height = 10, selectmode = "browse")
    
        scrollb = ttk.Scrollbar(panelPaginaJogo,orient="vertical",command=tview3.yview)
        scrollb.place(x=605,y=160,height=225)
        tview3.configure(yscrollcommand=scrollb.set)
    
        tview3.column("Utilizador", width = 100, anchor = "c")
        tview3.column("Comentário", width = 450, anchor = "c")
    
        tview3.heading("Utilizador", text = "Utilizador")
        tview3.heading("Comentário", text = "Comentário")
        tview3.place(x=50, y=160)
    
        CommentBox = Text(panelPaginaJogo,height=3,width=60)
        CommentBox.place(x=50,y=400)
    
        btnCommentar = Button(panelPaginaJogo, width=10, height=3,text="Comentar")
        btnCommentar.place(x=540,y=400)

    window=Toplevel()
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    appWidth = 1000                             
    appHeight = 500 
    x = (screenWidth/2) - (appWidth/2)     
    y = (screenHeight/2) - (appHeight/2)
    window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    window.title('Catálogo')

    panelOpcoes = PanedWindow(window, bg = "gray", width=250, height=500)
    panelOpcoes.place(x=0, y=0)

    imageGerir = PhotoImage(file = "images\\gerir.png")
    btnOpcaoGerir = Button(panelOpcoes, text = "Gerir os\nmeus jogos", image = imageGerir, compound=LEFT, relief = "sunken",width = 230, height = 68, font="calibri, 11",command=containerGerirJogos)
    btnOpcaoGerir.place (x=5, y=130)

    imageConsulta = PhotoImage(file = "images\\consultar.png" )
    btnOpcao2 = Button(panelOpcoes, text = "Consultar \nJogos", relief = "sunken", image = imageConsulta, compound=LEFT,width = 230, height = 68,  font="calibri, 11",command=containerConsultarJogos)
    btnOpcao2.place (x=5, y=210)

    containerGerirJogos()

    window.mainloop()
############################ CATALOGO FIM ###############################
############################ WINDOW ###############################
main=Tk()

# Window placement code
screenWidth = main.winfo_screenwidth()
screenHeight = main.winfo_screenheight()

appWidth = 1100
appHeight = 600

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

main.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

main.title("Main Page")
main.resizable(0,0)

############################ ELEMENTS ###############################
# Image Canvas
ctnImage = Canvas(main, width=700, height=800)
ctnImage.place(x=468, y=152)

img = PhotoImage(file="images\main_img.png")
ctnImage.create_image(0, 0, anchor="nw", image=img)

# Paned Window Buttons
panel1 = PanedWindow(main, height=600, width=448, bg="dark grey")
panel1.place(x=0, y=0)

# Button Log In Page
btn_Login = Button(main, text="Iniciar Sessão", fg="blue", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), command=logInPg)
btn_Login.place(x=720, y=40)

# Button Log In Page
btn_SignUp = Button(main, text="Criar Conta", fg="blue", relief="raised", bd=3, width=15, height=2, font=("TkDefaultFont", "12", "bold"), command=signUpPg)
btn_SignUp.place(x=890, y=40)

# Button Catalogue
imageIconCat = PhotoImage(file="images\\catal_img.png")
btn_cat = Button(panel1, text="Catálogo", fg="blue", relief="raised", bd=3, width=300, height=80, font=("TkDefaultFont", "20", "bold"), image=imageIconCat, compound=RIGHT,command=abrirCatalogo)
btn_cat.place(x=80, y=40)

# Button Search
imageIconSearch = PhotoImage(file="images\\search_img.png")
btn_ser = Button(panel1, text="Pesquisa", fg="blue", relief="raised", bd=3, width=300, height=80, font=("TkDefaultFont", "20", "bold"), image=imageIconSearch, compound=RIGHT)
btn_ser.place(x=80, y=150)

# Button User Profile
imageIconUser = PhotoImage(file="images\\user_img.png")
btn_user = Button(panel1, text="Perfil de Utilizador", fg="blue", relief="raised", bd=3, width=300, height=80, font=("TkDefaultFont", "20", "bold"), image=imageIconUser, compound=RIGHT)
btn_user.place(x=80, y=260)

# Button Close
imageIconClose = PhotoImage(file="images\\close_img.png")
btn_close = Button(panel1, text="Sair", fg="blue", relief="raised", bd=3, width=300, height=80, font=("TkDefaultFont", "20", "bold"), image=imageIconClose, compound=RIGHT, command=main.destroy)
btn_close.place(x=80, y=370)

############################ MAINLOOP ###############################
main.mainloop()