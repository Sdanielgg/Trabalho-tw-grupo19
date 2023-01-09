from tkinter import *
class Application:
    def __init__(self, master=None):
        pass
window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1000                             
appHeight = 500 
x = (screenWidth/2) - (appWidth/2)        
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('Favoritos')
panelOpçoes = PanedWindow(window, bg = "gray", width=250, height=500)
panelOpçoes.place(x=0, y=0)
#label frames

lbfmain=LabelFrame(window,width=170,height=100)
lbfmain.place(x=600,y=100,anchor=CENTER)
lbfsecondary=LabelFrame(window,width=650,height=250)
lbfsecondary.place(x=600,y=300,anchor=CENTER )
#label fav
lbjogos_favoritos=Label(lbfmain,text='Jogos Favoritos Totais:',font='calibri, 11')
lbjogos_totais_num=Label(lbfmain,text='(Nºjogos favoritos totais)',font='calibri, 10')
lbjogos_favoritos.place(x=5,y=10)
lbjogos_totais_num.place(x=15,y=40)
    #jogos de Ação
lbfav1=Label(lbfsecondary,text='Fav1:nd',font='calibri, 10')
lbfav1.place(x=25,y=50)
    #jogos de Corrida
lbfav2=Label(lbfsecondary,text='Fav2:nd',font='calibri, 10')
lbfav2.place(x=200,y=50)
    #jogos FPS
lbfav3=Label(lbfsecondary,text='Fav3:nd',font='calibri, 10')
lbfav3.place(x=400,y=50)
    #jogos RPG
lbfav4=Label(lbfsecondary,text='Fav4:nd',font='calibri, 10')
lbfav4.place(x=575,y=50)
    #jogos Battle Royale    
lbfav5=Label(lbfsecondary,text='Fav5:nd',font='calibri, 10')
lbfav5.place(x=25,y=170)
    #jogos de Desporto
lbfav6=Label(lbfsecondary,text='Fav6:nd',font='calibri, 10')
lbfav6.place(x=200,y=170)
    #jogos de Simulação
lbfav7=Label(lbfsecondary,text='Fav7:nnd',font='calibri, 10')
lbfav7.place(x=400,y=170)
    #jogos de estrategia
lbfav8=Label(lbfsecondary,text='Fav8:nd',font='calibri, 10')
lbfav8.place(x=575,y=170)




mainloop()
