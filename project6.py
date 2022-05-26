#Simple Digital Clock 
from tkinter import*
from tkinter.ttk import*

from time import strftime

#Creating Thinter Window
root = Tk()
root.title("Clock")
#It Show The Time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
#Create A Label To Store The Clock
label=Label(root,font = ("ds-digital",80,"bold"), background="black", foreground="cyan")
#Background For Background Color And Foreground For Clock Color.
label.pack(anchor='center')

time()
mainloop()