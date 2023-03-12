
from tkinter import *

app=Tk()
app.title("To-Do-List")
app.geometry("400x650+400+100")

workload_list = []


def WorkloadFile():
    with open("workload.txt","r") as taskfile:               #With open function means it tells the computer to open and read the workload.txt file
        workloads = taskfile.readlines()                     #Readline method means it returns one line from the file.


# In this code, python for loop is used to run it's block of code multiple times until it reaches and reads the last item.In this example below, the variable workload tries to access each item inside the workloads text file on an iterated loop. !='\'n' means it's evaluated as true if the last item is different to a new line last item is encountered. When the new line which appears to be the last line of the text file, it gets added onto the workload_list array. It adds the workload_list array onto the listbox. 


    for workload in workloads:                             
        if workload !='\n':
            workload_list.append(workload)
            listbox.insert(END, workload)
            

#to-do-list application icon

Image_logo=PhotoImage(file="Image_Object/task.png")
app.iconphoto(False, Image_logo)

#to-do-list application top bar

TopImage=PhotoImage(file="Image_Object/topbar.png")
Label(app,image=TopImage).pack()

#to-do-list dock image
dockImage=PhotoImage(file="Image_Object/dock.png")
Label(app,image=dockImage,bg="#CCFFAB").place(x=30,y=20)

#Adding the logo onto the to-do-list application
TaskImage=PhotoImage(file="Image_Object/task.png")
Label(app,image=TaskImage,bg="#CCFFAB").place(x=340,y=20)

#Creating a title for the to-do-list application
title=Label(app, text="TASK LIST",font="arial 20 bold",fg="black",bg="#CCFFAB")
title.place(x=130,y=15)

#Creating a text box

textbox= Frame(app,width=400,height=43,bg="white", bd=0)
textbox.place(x=0,y=140)

write=StringVar()
write_entry=Entry(textbox,width=20,font="arial 18")
write_entry.place(x=10,y=5)

#Creating a button on this application

button=Button(app,text="ADD",font="arial 20",bd=0, width=6, bg="#5a95ff", fg="#fff")
button.place(x=300,y=140)

#Creating a listbox to store the list 

padding = Frame(app,bd=3,width=700,height=280,bg="#CCFFAB")
padding.pack(pady=(120,0))

listbox = Listbox(padding,font=('arial',12),width=40,height=16,bg="#CCFFAB", bd=0, fg="black", cursor="hand2", selectbackground="#CCFFAB")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(padding)
scrollbar.pack(side= RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

WorkloadFile()

#Task delete button
Delete=PhotoImage(file="Image_Object/delete.png")
Button(app,image=Delete,bd=0).pack(side=BOTTOM,pady=13)



app.mainloop()

