import tkinter as tk
from tkinter import ttk

window = tk. Tk()
window.geometry("600x300")
window.title("Label")

inputVar = tk.StringVar()
userName_Entry = ttk. Entry(window,textvariable=inputVar)        # entry box ki value inputVar variable me ja rhi h
b1 = ttk.Button(window,text="show value", command=lambda :print(inputVar.get()))

userName_Entry.pack()
b1.pack()

window.mainloop()