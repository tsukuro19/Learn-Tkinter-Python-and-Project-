from tkinter import *

root=Tk()
root.title("Calculator")

e=Entry(root,width=35,borderwidth=5)
#difference between column and columnspan:https://stackoverflow.com/questions/50158866/what-is-the-difference-between-column-and-columnspan-in-tkinter-python
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)#colmnspan:How many columns widget occupies

def Click_button(number):
    #e.delete used to delete what's already in the box
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def Add_button():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    e.delete(0,END)

def Clear_number():
    e.delete(0,END)

def Equal_button():
    second_number=e.get()
    e.delete(0,END)
    e.insert(0,f_num+int(second_number))

def Create_function():
    button_add=Button(root,text="+",padx=39,pady=20,command=Add_button)
    button_clear=Button(root,text="Clear",padx=79,pady=20,command=Clear_number)
    button_equal=Button(root,text="=",padx=91,pady=20,command=Equal_button)
    button_add.grid(row=5,column=0)
    button_equal.grid(row=5,column=1,columnspan=2)
    button_clear.grid(row=4,column=1,columnspan=2)

def create_button():
    buttons=[]
    for i in range(10):
        #Read more lambda:https://www.w3schools.com/python/python_lambda.asp
        new_button=Button(root,text=""+str(i),padx=40,pady=20,command=lambda c=i: Click_button(c))
        buttons.append(new_button)
    return buttons

def grid_button(buttons):
    index=1
    for rows in range(3,0,-1):
        for cols in range(0,3):
            buttons[index].grid(row=rows,column=cols)
            index+=1
    buttons[0].grid(row=4,column=0)

if __name__=="__main__":
    buttons=create_button()
    grid_button(buttons)
    Create_function()
    root.mainloop()
