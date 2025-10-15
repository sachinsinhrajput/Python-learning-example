import tkinter as tk
import tkinter as ttk
from time import strftime
root = tk.Tk()
root.title("Digital Clock")

def time():
    string=strftime(' %b %d,%Y\n %I:%M:%S %p\n %A')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl=tk.Label(root,font=('calibri',20,'bold'),
            background='black',
            foreground='white')

lbl.pack(ancho='center')
time() 
root.mainloop()
   