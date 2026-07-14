import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("grid layout")
window.geometry("500x500")

label1 = ttk.Label(window, text="Label1", background="red")
label2 = ttk.Label(window, text="Label2", background="green")
label3 = ttk.Label(window, text="Label3", background="blue")
label4 = ttk.Label(window, text="Label4", background="yellow")
label5 = ttk.Label(window, text="Label5", background="orange")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2,weight=1)

# place
label1.grid(row=0, column=0,sticky="nswe")
label2.grid(row=0, column=1,sticky="nswe")
label3.grid(row=1, column=0,sticky="nswe")
#label4.grid(row=1, column=1,sticky="nswe",rowspan=2)        two row lelega
label4.grid(row=1, column=1,sticky="nswe",rowspan=2) 
#label5.grid(row=2, column=0,sticky="nswe",columnspan=2)   ye do column lega
label5.grid(row=2, column=0,sticky="nswe")


window.mainloop()