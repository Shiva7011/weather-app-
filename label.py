import tkinter as tk
from tkinter import ttk

window = tk. Tk()
window.geometry("600x300")
window.title("Label")


textvar=tk.StringVar(value="shiva singh")      #stringvar ki priority jyada hoti h isi liye ye show hota h text ki bjaye

label1 = ttk.Label(window,
           text="sbs online classes",             #ye text tha label ka jo textvar ne overwrite kar dia
           font=("calibri",20,"bold"),
           background="blue",
           foreground="white",
           padding=10,
           textvariable=textvar
)

b1=ttk.Button(window,text="change button",command= lambda : textvar.set("changed ho gya"))      #yaha se humne change kar dia text
label1.pack()
b1.pack()

window.mainloop()