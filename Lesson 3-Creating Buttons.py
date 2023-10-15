#read more:https://www.tutorialspoint.com/python/tk_button.htm
from tkinter import *

root=Tk()

def myClick():
    myLabel=Label(root,text="Hehe, i clicked button",fg="blue")
    myLabel.pack()

#creating label
myButton=Button(root,text="Click me",command=myClick,fg="red",bg="blue")#option:state for activate button,padx,y for padding button,command: call function 
myButton.pack()

root.mainloop()