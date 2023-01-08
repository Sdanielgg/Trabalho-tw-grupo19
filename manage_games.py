# Manage Games
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox

############################ FUNCTIONS ###############################


############################ WINDOW ###############################
manageGames=Tk()

# Window placement code
screenWidth = manageGames.winfo_screenwidth()
screenHeight = manageGames.winfo_screenheight()

appWidth = 900
appHeight = 350

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)

manageGames.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

manageGames.title("Manage Games Page")
manageGames.resizable(0,0)

############################ ELEMENTS ###############################
# Menu Barra
barra_Menu = Menu(manageGames)

# Games Menu Cascade
games_Menu = Menu(barra_Menu)
games_Menu.add_command(label="Catalogue", command="noaction")
games_Menu.add_command(label="Search", command="noaction")
barra_Menu.add_cascade(label="Games", menu=games_Menu)

# User Menu Cascade
user_Menu = Menu(barra_Menu)
user_Menu.add_command(label="User Profile", command="noaction")
user_Menu.add_command(label="Favourites", command="noaction")
barra_Menu.add_cascade(label="User", menu=user_Menu)

# Admin Menu Cascade
admin_Menu = Menu(barra_Menu)
admin_Menu.add_command(label="Manage Users", command="noaction")
admin_Menu.add_command(label="Manage Games", command="noaction")
barra_Menu.add_cascade(label="Admin", menu=admin_Menu)

# Close Option
barra_Menu.add_command(label="Sair", command=manageGames.quit)

manageGames.configure(menu=barra_Menu)

# LabelFrame Filter
frame1 = LabelFrame(manageGames, text="Filters", fg="red", width=300, height=210, relief="sunken", bd=3)
frame1.place(x=10, y=10)

# Label Entry Game Name
lbl_gameName = Label(frame1, text="Game Name:", fg="blue")
lbl_gameName.place(x=20, y=30)

# Entry Game Search
txt_gameName = Entry(frame1, width=25)
txt_gameName.place(x=110, y=30)

# Label Category 
lbl_gameCat = Label(frame1, text="Category:", fg="blue")
lbl_gameCat.place(x=20, y=80)

# Combobox Category
categoryList = ["Category1", "Category2", "Category3"]
cb_category = Combobox(frame1, values=categoryList)
cb_category.place(x=110, y=80)

# Button Search
btn_search = Button(frame1, text="Filter", fg="red", width=15, height=2)
btn_search.place(x=120, y=130)

# Button Delete Game
btn_del = Button(manageGames, text="Delete Selected", fg="blue", width=25, height=3)
btn_del.place(x=40, y= 250)

# Treeview Game
panel1 = PanedWindow(manageGames, width=550, height=300, relief="sunken", bd=2)
panel1.place(x=330, y=20)

global tree
tree = ttk.Treeview(panel1, selectmode="browse", columns=("Name", "Category", "Rating", "No. of Ratings"), show="headings", height=300)

tree.column("Name", width=155, anchor="c")
tree.heading("Name", text="Name")

tree.column("Category", width=130, anchor="c")
tree.heading("Category", text="Category")

tree.column("Rating", width=130, anchor="c")
tree.heading("Rating", text="Rating")

tree.column("No. of Ratings", width=130, anchor="c")
tree.heading("No. of Ratings", text="No. of Ratings")

tree.place(x=0, y=0)

############################ MAINLOOP ###############################
manageGames.mainloop()