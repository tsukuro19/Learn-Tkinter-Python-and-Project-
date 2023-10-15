from tkinter import *

root=Tk()

#creating label
Hello_label=Label(root,text="Hello world")
myLabel=Label(root,text="My name is hello")

#shoving label as coordinate onto the screen
myLabel.grid(row=0,column=0)#grid as a matrix to locate label,button... it activity as table 2 dimensional
Hello_label.grid(row=1,column=0)

#event loop
root.mainloop()
