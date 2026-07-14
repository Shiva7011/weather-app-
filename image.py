import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


window = tk. Tk()
window.geometry("600x300")
window.title("Label")

#Load image
image_path = "screenshot.png"
img = Image.open(image_path)

#resize
resizedImage = img.resize((100,50))

#display
tk_image = ImageTk.PhotoImage(img)           #agar resized image dikhani h to resizedImage variable dalenge

label1 = ttk.Label(window,image=tk_image)
label1.pack()


window.mainloop()