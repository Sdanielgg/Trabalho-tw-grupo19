# Login
from tkinter import *
from tkinter import messagebox
import os
############################ FUNCTIONS ###############################
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

def abriCatalogo():
    os.startfile("catalogo.py")

    ############################ ELEMENTS ###############################

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

    ############################ MAINLOOP ###############################
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
btn_cat = Button(panel1, text="Catálogo", fg="blue", relief="raised", bd=3, width=300, height=80, font=("TkDefaultFont", "20", "bold"), image=imageIconCat, compound=RIGHT,command=abriCatalogo)
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