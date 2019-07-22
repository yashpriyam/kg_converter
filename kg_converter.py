from tkinter import *  #import * = import all from tkinter

window=Tk()     #it creates a window// 'Tk' is correct not 'tk'
def kg_conv():
       #e1_value is an object, .get is a function to get the string entrered in entry widget
    grams=float(e1_value.get())*1000
    t1.delete("1.0", END)
    t1.insert(END,grams)   #to put the value entered in text widget at the end of it.what'er you enter in entry widget you get that in text
    pounds=float(e1_value.get())*2.20462
    t2.delete("1.0", END)
    t2.insert(END,pounds)
    ounces=float(e1_value.get())*35.274
    t3.delete("1.0", END)
    t3.insert(END,ounces)
b1=Button(window,text="Convert",command=kg_conv)   #defining a variable, button creates a button in windows with name 'execute' written on it and we can pass 'text' in it
                                                        #command function helps you execute any function through your button
b1.grid(row=0,column=4)       #b1.pack() places the button in the window or can use b1.grid(row=0,column=0)#much better method

e1_value=StringVar()    #StringVar is a fuction to denote e1_value is a string variable
e1=Entry(window,textvariable=e1_value)    #creates entry bar in your window where you can type in any data (text),textvariable ensures it is a text
e1.grid(row=0,column=2)     #rows=(),column=() decide place of the button in the window
e2=Label(window,text="kg")
e2.grid(row=0,column=0)
e3=Label(window,text="grams")
e3.grid(row=1,column=0)
e4=Label(window,text="pounds")
e4.grid(row=1,column=2)
e5=Label(window,text="ounces")
e5.grid(row=1,column=4)

t1=Text(window,height=1,width=10)  #height=(),width=() decides size of the widget in your window
t1.grid(row=1,column=1) #location of t1 in the window
t2=Text(window,height=1,width=10)
t2.grid(row=1,column=3)
t3=Text(window,height=1,width=10)
t3.grid(row=1,column=5)
window.mainloop()   #all the program written between these window commands is shown in the window
