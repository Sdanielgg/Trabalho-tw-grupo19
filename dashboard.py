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
window.title('Dashboard')
#9 labels a dizer informação (informação vai mudando pq ainda nao sabemos o numero de jogos que vamos ter).
panelOpçoes = PanedWindow(window, bg = "gray", width=250, height=500)
panelOpçoes.place(x=0, y=0)
#label frames
lbfmain=LabelFrame(window,width=150,height=100)
lbfmain.place(x=600,y=100,anchor=CENTER)
lbfsecondary=LabelFrame(window,width=650,height=260)
lbfsecondary.place(x=600,y=300,anchor=CENTER )
#labels estatisticas
    #jogos totais
lbjogos_totais=Label(lbfmain,text='Jogos Totais:',font='calibri, 11')
lbjogos_totais_num=Label(lbfmain,text='(Nºjogos totais)',font='calibri, 11')
lbjogos_totais.place(x=20,y=10)
lbjogos_totais_num.place(x=20,y=40)
    #jogos de Ação
lbAção=Label(lbfsecondary,text='Jogos de Ação:nd',font='calibri, 10')
lbAção.place(x=20,y=50)
    #jogos de Corrida
lbCorrida=Label(lbfsecondary,text='Jogos de Corrida:nd',font='calibri, 10')
lbCorrida.place(x=180,y=50)
    #jogos FPS
lbFPS=Label(lbfsecondary,text='Jogos Fps:nd',font='calibri, 10')
lbFPS.place(x=330,y=50)
    #jogos RPG
lbRPG=Label(lbfsecondary,text='Jogos RPG:nd',font='calibri, 10')
lbRPG.place(x=490,y=50)
    #jogos Battle Royale    
lbBattle_Royale=Label(lbfsecondary,text='Jogos Battle Royale:nd',font='calibri, 10')
lbBattle_Royale.place(x=20,y=170)
    #jogos de Desporto
lbDesporto=Label(lbfsecondary,text='Jogos de Desporto:nd',font='calibri, 10')
lbDesporto.place(x=180,y=170)
    #jogos de Simulação
lbSimulação=Label(lbfsecondary,text='Jogos de Simulação:nnd',font='calibri, 10')
lbSimulação.place(x=330,y=170)
    #jogos de estrategia
lbEstrategia=Label(lbfsecondary,text='Jogos de Estrategia:nd',font='calibri, 10')
lbEstrategia.place(x=490,y=170)




mainloop()