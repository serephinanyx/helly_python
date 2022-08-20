
import tkinter

screen=tkinter.Tk()

screen.geometry("600x500")
screen.configure(bg="purple")

#tkinter variable

var_num=tkinter.IntVar()
count=0

def mydef():
    global count

    count+=1
    print("your review:",count)

def myfun():
    global count
    count-=1
    print("your review:",count)


 
print("your choice",var_num.get())

#label

lbl=tkinter.Label(screen,text="welcome to your review",font=("arial",26,"bold"),bg="purple")
lbl.place(x=80,y=10)

#entry

e1=tkinter.Entry(screen,textvariable=var_num)
e1.place(x=160,y=80)

#button

btn1=tkinter.Button(screen,text="like",font=("arial",10,"bold"),command=mydef)
btn1.place(x=100,y=150)
btn2=tkinter.Button(screen,text="dislike",font=("arial",10,"bold"),command=myfun)
btn2.place(x=150,y=150)


#label
lbl_name = tkinter.Label(screen,text="total like :",font=("arial",10,"bold"),bg="purple")
lbl_name.place(x=20,y=80)

screen.mainloop()