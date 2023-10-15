#Read more:https://www.tutorialspoint.com/python/tk_entry.htm
from tkinter import *
root=Tk()

def myClick():
    myLabel=Label(root,text="Hello, "+e.get())#e.get() will take content in input field
    myLabel.pack() 

#creating input field
e=Entry(root,width=50,borderwidth=5)
e.pack()
e.insert(0,"Enter your name: ")#used to create content available in field entry

myButton=Button(root,text="Enter your name",fg="red",command=myClick)
myButton.pack()

if __name__=="__main__":
    root.mainloop()