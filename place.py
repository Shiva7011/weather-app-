import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("pack layout")
window.geometry("500x500")

label1 = ttk.Label(window, text="Label1", background="red")

label1.place(x=100, y=300)   #mtlb left se 100 pixel aur top se 300 pixel ki jagah pe label1 ko place karega
#label1.place(relx=0.1, rely=0.2)  #mtlb label1 ko window ke center me place karega

label1.place(relx=0, rely=0, relwidth=0.2, relheight=0.2)



window.mainloop()