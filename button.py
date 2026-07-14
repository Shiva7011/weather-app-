import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("button")
window.geometry("500x500")

def buttonClicked():
    print("hello")

b1 = ttk.Button(window,text="click here",padding=10, command=buttonClicked)
b1.pack()

#less use hota h 
#def buttonClicked():
 #   buttonVar.set("ok")  

#buttonVar = tk.StringVar(value="click me")
#b1 = ttk.Button(window,text="click here",padding=10, command=buttonClicked, textvariable=buttonVar)
#b1.pack()

window.mainloop()