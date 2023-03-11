
from tkinter import *

app=Tk()
app.title("To-Do-List")
app.geometry("400x650+400+100")

tasklist = []

#to-do-list application icon

Image_logo=PhotoImage(file="Image_Object/task.png")
app.iconphoto(False, Image_logo)

#to-do-list application top bar

TopImage=PhotoImage(file="Image_Object/topbar.png")
Label(app,image=TopImage).pack()

#to-do-list dock image
dockImage=PhotoImage(file="Image_Object/dock.png")
Label(app,image=dockImage,bg="#32405b").place(x=30,y=25)

#Adding the logo onto the to-do-list application
TaskImage=PhotoImage(file="Image_Object/task.png")
Label(app,image=TaskImage,bg="#32405b").place(x=340,y=25)

#Creating a title for the to-do-list application
title=Label(app, text="TASK LIST",font="arial 20 bold",fg="white",bg="#32405b")
title.place(x=130,y=20)

#list (main)

textbox= Frame(app,width=400,height=50,bg="white", bd=0)
textbox.place(x=0,y=180)

write=StringVar()
write_entry=Entry(textbox,width=18,font="arial 20")
write_entry.place(x=10,y=7)

app.mainloop()

