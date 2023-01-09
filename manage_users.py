# Manage Users
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

############################ FUNCTIONS ###############################


############################ WINDOW ###############################
manageUsers=Tk()

# Window placement code
screenWidth = manageUsers.winfo_screenwidth()
screenHeight = manageUsers.winfo_screenheight()

appWidth = 830
appHeight = 350

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

manageUsers.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

manageUsers.title("Manage Users Page")
manageUsers.resizable(0,0)

############################ ELEMENTS ###############################
# Menu Barra
barra_Menu = Menu(manageUsers)

# Games Menu Cascade
games_Menu = Menu(barra_Menu)
games_Menu.add_command(label="Catálogo", command="noaction")
games_Menu.add_command(label="Pesquisa", command="noaction")
barra_Menu.add_cascade(label="Jogos", menu=games_Menu)

# User Menu Cascade
user_Menu = Menu(barra_Menu)
user_Menu.add_command(label="Perfil de Utilizador", command="noaction")
user_Menu.add_command(label="Favoritos", command="noaction")
barra_Menu.add_cascade(label="Utilizador", menu=user_Menu)

# Admin Menu Cascade
admin_Menu = Menu(barra_Menu)
admin_Menu.add_command(label="Gerir Utilizadores", command="noaction")
admin_Menu.add_command(label="Gerir Jogos", command="noaction")
barra_Menu.add_cascade(label="Admin", menu=admin_Menu)

# Close Option
barra_Menu.add_command(label="Sair", command=manageUsers.quit)

manageUsers.configure(menu=barra_Menu)

# LabelFrame Filter
frame1 = LabelFrame(manageUsers, text="Filtros", fg="red", width=300, height=210, relief="sunken", bd=3)
frame1.place(x=30, y=10)

# Label Entry Game Name
lbl_gameName = Label(frame1, text="Username:", fg="blue")
lbl_gameName.place(x=20, y=30)

# Entry Game Search
txt_gameName = Entry(frame1, width=25)
txt_gameName.place(x=110, y=30)

# Radio Button User Type
selected = StringVar()
selected.set("user")
rd1 = Radiobutton(frame1, text="User", value="user", variable=selected)
rd2 = Radiobutton(frame1, text="Admin", value="admin", variable=selected)
rd1.place(x=50, y=80)
rd2.place(x=130, y=80)

# Button Search
btn_search = Button(frame1, text="Filtrar", fg="red", width=15, height=2)
btn_search.place(x=120, y=130)

# Button Delete Game
btn_del = Button(manageUsers, text="Apagar Seleção", fg="blue", width=25, height=3)
btn_del.place(x=80, y= 250)

# Treeview Users
panel1 = PanedWindow(manageUsers, width=420, height=300, relief="sunken", bd=2)
panel1.place(x=350, y=20)

global tree
tree = ttk.Treeview(panel1, selectmode="browse", columns=("Tipo de Utilizador", "Username", "Password"), show="headings", height=300)

tree.column("Tipo de Utilizador", width=155, anchor="c")
tree.heading("Tipo de Utilizador", text="Tipo de Utilizador")

tree.column("Username", width=130, anchor="c")
tree.heading("Username", text="Username")

tree.column("Password", width=130, anchor="c")
tree.heading("Password", text="Password")

tree.place(x=0, y=0)
############################ MAINLOOP ###############################
manageUsers.mainloop()