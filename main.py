
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

#Creating a text box

textbox= Frame(app,width=400,height=43,bg="white", bd=0)
textbox.place(x=0,y=180)

write=StringVar()
write_entry=Entry(textbox,width=20,font="arial 18")
write_entry.place(x=10,y=5)

#Creating a button on this application

button=Button(app,text="ADD",font="arial 20",bd=0, width=6, bg="#5a95ff", fg="#fff")
button.place(x=300,y=180)

#Creating a listbox to store the list 

padding = Frame(app,bd=3,width=700,height=280,bg="#32405b")
padding.pack(pady=(160,0))

listbox = Listbox(padding,font=('arial',12),width=40,height=16,bg="#32405b", bd=0, fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(padding)
scrollbar.pack(side= RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


#Task delete button
Delete=PhotoImage(file="Image_Object/delete.png")
Button(app,image=Delete,bd=0).pack(side=BOTTOM,pady=13)



app.mainloop()

