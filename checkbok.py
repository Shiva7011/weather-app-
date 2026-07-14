import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("button")
window.geometry("500x500")


cLabelVar = tk. StringVar()
c = ttk.Checkbutton(window,text="i agree")
c.pack()




window.mainloop()