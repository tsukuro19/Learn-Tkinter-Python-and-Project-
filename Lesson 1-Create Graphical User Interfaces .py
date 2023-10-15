#read more:https://realpython.com/python-gui-tkinter/
#https://tkdocs.com/tutorial/index.html
#Read more about label:https://www.tutorialspoint.com/python/tk_label.htm
from tkinter import *

root=Tk()#alway use this to can use tkinter in every operation

#creating a label by widget
label=Label(root,text='Hello world')#method create label
#shoving(đẩy) it onto the screen
label.pack()#this method will pack label and put it to widget(root)

#create a event loop of program
root.mainloop()