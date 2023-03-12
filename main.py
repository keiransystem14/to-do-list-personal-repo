
from tkinter import *

app=Tk()
app.title("To-Do-List")
app.geometry("400x650+400+100")

#array
workload_list = []


#This means it defines a function called addworkload(), workload vairable is used to get information that was entered onto the single line textbox. write_entry.delete function is used to clear the the information entered on the signle line textbox after the add button is pressed. 

#'if workload' statement means if information is entered on the single line textbox on the application, it opens the file called workload.txt and writes the item from the single line textbox. It then appends the item from the new line onto the array called workload_list.

def addWorkload():
    workload = write_entry.get()
    write_entry.delete(0, END)

    if workload:
        with open("workload.txt","a") as taskfile:
            taskfile.write(f"\n{workload}")
        workload_list.append(workload)
        listbox.insert(END, workload)
        

#It defines a function called "deleteWorkload()". Inside the function, it uses the global variable to globally access the workload_list array while the application is running. It then gets the positional point of where the text is inside the listbox. 

#It uses the IF statement to check if the text is inside the listbox.If it's true then it opens the workload.txt file and deletes that specific item from that text file. It then updates the listbox and displays what's inside the workload.txt file. 


def deleteWorkload():
    global workload_list
    workload = str(listbox.get(ANCHOR))
    if workload in workload_list:
        workload_list.remove(workload)
        with open("workload.txt", 'w') as taskfile:
            for workload in workload_list:
                taskfile.write(workload+"\n")
                
            listbox.delete(ANCHOR)


def openWorkloadFile():

    try:

        global workload_list

        with open("workload.txt","r") as taskfile:               #With open function means it tells the computer to open and read the workload.txt file
            workloads = taskfile.readlines()                     #Readline method means it returns one line from the file.


# In this code, python for loop is used to run it's block of code multiple times until it reaches and reads the last item.In this example below, the variable workload tries to access each item inside the workloads text file on an iterated loop. !='\'n' means it's evaluated as true if the last item is different to a new line last item is encountered. When the new line which appears to be the last line of the text file, it gets added onto the workload_list array. It adds the workload_list array onto the listbox. 


        for workload in workloads:                             
            if workload !='\n':
                workload_list.append(workload)
                listbox.insert(END, workload)
            
    except:
        file= open('workload.txt','w')
        file.close()

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

#Creating a button on this application. The add button uses the addworkload function to perform the following actions after entering words into the single line textbox.

button=Button(app,text="ADD",font="arial 20",bd=0, width=6, bg="#5a95ff", fg="#fff", command=addWorkload)
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

openWorkloadFile()

#Task delete button
Delete=PhotoImage(file="Image_Object/delete.png")
Button(app,image=Delete,bd=0, command=deleteWorkload).pack(side=BOTTOM,pady=13)



app.mainloop()

