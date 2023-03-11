
from tkinter import *

app=Tk()
app.title("To-Do-List")
app.geometry("400x650+400+100")

tasklist = []

#to-do-list application icon

Image_logo=PhotoImage(file="Image_Object/sketch-3-todo-list-app-icon-template.png")
app.iconphoto(False, Image_logo)

#to-do-list application top bar

TopImage=PhotoImage(file="Image_Object/topbar.png")
Label(app,image=TopImage).pack()

#to-do-list dock image
dockImage=PhotoImage(file="Image_Object/dock.png")
Label(app,image=dockImage,bg="#32405b").place(x=30,y=25)


app.mainloop()

