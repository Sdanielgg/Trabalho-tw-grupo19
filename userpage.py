from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

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
window.title('Pagina de utilizador')

panelOpçoes = PanedWindow(window, bg = "gray", width=250, height=500)
panelOpçoes.place(x=0, y=0)
#utilizador
panelfoto=PanedWindow(window,bg='blue',width=60,height=60)
panelfoto.place(x=270,y=10)
txtnome=Label(window,text='Nome',font='Helvetica, 20')
txtperms=Label(window,text='user',font='Calibri, 7')
txtnome.place(x=330,y=2)
txtperms.place(x=330,y=55)
#preferencias
lbpref=Label(window,text='Generos Favoritos:(Recebera notificações de novidades sobre estes generos)',font='Calibri, 9')
lbpref.place(x=290,y=100)
    #CheckButtons
checkVar1 = IntVar()
checkVar2 = IntVar()
checkVar3 = IntVar()
checkVar4 = IntVar()
checkVar5 = IntVar()
checkVar6 = IntVar()
checkVar7 = IntVar()
checkVar8 = IntVar()
cb1=Checkbutton(window, text='Ação', variable=checkVar1)
cb2=Checkbutton(window, text='Corrida', variable=checkVar2)
cb3=Checkbutton(window, text='FPS', variable=checkVar3)
cb4=Checkbutton(window, text='RPG', variable=checkVar4)
cb5=Checkbutton(window, text='Battle Royale', variable=checkVar5)
cb6=Checkbutton(window, text='Desporto', variable=checkVar6)
cb7=Checkbutton(window, text='Simulação', variable=checkVar7)
cb8=Checkbutton(window, text='Estrategia', variable=checkVar8)
cb1.place(x=300,y=140)
cb2.place(x=400,y=140)
cb3.place(x=500,y=140)
cb4.place(x=600,y=140)
cb5.place(x=300,y=200)
cb6.place(x=400,y=200)
cb7.place(x=500,y=200)
cb8.place(x=600,y=200)
#logout
btnlogout=Button(window,text='Logout',width=20)
btnlogout.place(x=300,y=450)




mainloop()