from tkinter import*
top=Tk()
def hello():
    print("hello")

#create toplevel menu
menubar=Menu(top)
menubar.add_command(label="Hello!",command=hello)
menubar.add_command(label="Quit!",command=quit)

#display the menu
top.config(menu=menubar)
top.mainloop()