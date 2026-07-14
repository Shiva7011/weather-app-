import tkinter as tk
from tkinter import ttk

window = tk. Tk()
window. title("radio button")
window.geometry("300x100")
window.maxsize(height=400, width=600)

genderval=tk.StringVar()
r1 = ttk.Radiobutton(window, text="male",variable=genderval,value="m")
r2 = ttk.Radiobutton(window, text="female",variable=genderval,value="f")
r1.pack()
r2.pack()

window.mainloop()