from tkinter import*
top=Tk()
name=Label(top,text="Name").grid(row=0,column=0)
e1=Entry(top).grid(row=0,column=1)
password=Label(top,text="Password").grid(row=1,column=0)
e2=Entry(top).grid(row=1,column=1)
submit=Button(top,text="Submit").grid(row=4,column=0)
top.mainloop()