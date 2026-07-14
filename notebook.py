import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x300")
window.title("Notebook")

myNotebook = ttk.Notebook(window)

frame1 = ttk.Frame(myNotebook)
frame2 = ttk.Frame(myNotebook)
frame3 = ttk.Frame(myNotebook)

myNotebook.add(frame1, text="Tab 1")
myNotebook.add(frame2, text="Tab 2")
myNotebook.add(frame3, text="Tab 3")

myNotebook.pack(expand=True, fill="both")

label1 = ttk.Label(frame1, text="Tab 1 Content")
label2 = ttk.Label(frame2, text="Tab 2 Content")
label3 = ttk.Label(frame3, text="Tab 3 Content")

label1.pack(padx=30, pady=50)
label2.pack(padx=30, pady=50)
label3.pack(padx=30, pady=50)

window.mainloop()