import tkinter as tk
import tkinter as ttk

root = tk.Tk()
root.title("WEB-APP")
root.geometry("350x200")

lbl = tk.Label(root, text="welcome to my web-app")
lbl.grid()

btn = tk.Button(root, text="click me",fg="dark blue",bg="light green")
btn.grid()

txt=tk.Entry(root,width=10)
txt.grid(column=1   ,row=0)
root.mainloop()
