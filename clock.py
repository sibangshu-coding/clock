from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('simple clock')

def time():
    string = strftime('%H:%M:%S  - By Sibangshu Kundu')
    lbl.config(text = string),
    lbl.after(1000, time)

lbl = Label(root , font = ('calibri',40,'bold'),
            background = 'red',
            foreground = 'white')

lbl.pack(anchor = 'center')
time()
root.mainloop()
