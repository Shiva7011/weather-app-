
import tkinter as tk
from tkinter import ttk

window = tk. Tk()
window.geometry("600x300")
window.title("Label")

city_list =("Ranchi", "Bhubaneswar", "Delhi", "Chennai")

cityVar = tk.StringVar(value="select")

label1 = ttk.Label(window,text="city")
city_input = ttk.Combobox(window,textvariable=cityVar)
b1 = ttk.Button(window, text="show value", command=lambda : print(cityVar.get()))

city_input["values"] = city_list

label1.pack()
city_input.pack()
b1.pack()
window.mainloop()


