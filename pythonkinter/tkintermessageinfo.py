from tkinter import*
from tkinter import messagebox

top=Tk()

top.geometry("200x100")

def fun():
    messagebox.showinfo("Hello, Red button clicked")


b1=Button(top,text="Red",command=fun,activeforeground="red",activebackground="pink",pady=10)
b2=Button(top,text="Blue",activeforeground="blue",activebackground="pink",pady=10)
b3=Button(top,text="Green",activeforeground="green",activebackground="pink",pady=10)
b4=Button(top,text="Yellow",activeforeground="yellow",activebackground="pink",pady=10)

b1.pack(side=RIGHT)
b2.pack(side=LEFT)
b3.pack(side=BOTTOM)
b4.pack(side=TOP)

top.mainloop()