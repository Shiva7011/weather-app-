import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("pack")
window.geometry("500x500")

# Frame
frame1 = ttk.Frame(window, borderwidth=2, relief="solid")

# Labels
label1 = tk.Label(frame1, text="Label 1", bg="red")
label2 = tk.Label(frame1, text="Label 2", bg="green")
label1.pack(side="left", fill="both", expand=True)
label2.pack(side="left", fill="both", expand=True)

# widget
label3 = ttk.Label(window,text="label 3", background="yellow")

#frame2
frame2=ttk.Frame(window)
frame21=ttk.Frame(frame2)
frame22=ttk.Frame(frame2)

b1=ttk.Button(frame21,text="button1")
b2=ttk.Button(frame21,text="button2")
b3=ttk.Button(frame21,text="button3")

b1.pack(fill="both", expand=True)
b2.pack(fill="both", expand=True)
b3.pack(fill="both", expand=True)
frame21.pack(side="left",expand=True,fill="both")

label4=ttk.Label(frame22,text="label4",background="blue")
label4.pack(fill="both", expand=True)
frame22.pack(side="left",expand=True,fill="both")

#layout
frame1.pack(fill="both", expand=True)
label3.pack(fill="both", expand=True)
frame2.pack(fill="both",expand=True)




window.mainloop()