from tkinter import*
parent=Tk()
parent.geometry("400x250")
Name=Label(parent,text="Name").place(x=30,y=50)
email=Label(parent,text="Name").place(x=30,y=90)
password=Label(parent,text="Password").place(x=30,y=130)
e1=Entry(parent).place(x=80,y=50)
e2=Entry(parent).place(x=80,y=90)
e3=Entry(parent).place(x=100,y=130)
parent.mainloop()