from tkinter import *
from tkinter import ttk
import requests

def show_alert(title, message, temp=None):
    alert_window = Toplevel(win)
    alert_window.title(title)
    alert_window.geometry("400x200")
    alert_window.config(bg="#FF5252")
    alert_window.resizable(False, False)
    alert_window.transient(win)
    alert_window.grab_set()

    msg_label = Label(alert_window, text=message, font=("Segoe UI", 14, "bold"), fg="white", bg="#FF5252", wraplength=350)
    msg_label.pack(pady=20)

    if temp is not None:
        temp_label = Label(alert_window, text=f"Temperature: {temp}°C", font=("Segoe UI", 12), fg="white", bg="#FF5252")
        temp_label.pack(pady=10)

    close_btn = Button(alert_window, text="OK", font=("Segoe UI", 11, "bold"), command=alert_window.destroy, bg="#FF6B6B", fg="white", width=15)
    close_btn.pack(pady=10)

def get_weather():
    city = city_name.get().strip()
    if not city:
        w_label1.config(text="Enter city or select a state")
        wb_label1.config(text="")
        temp_label1.config(text="--")
        per_label1.config(text="--")
        return

    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=c388cc150ed05ef9537a21cf340dfcb4")
        data = response.json()
        if response.status_code != 200 or data.get("cod") != 200:
            raise ValueError(data.get("message", "City not found"))

        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"])
        temp = int(data["main"]["temp"] - 273.15)
        temp_label1.config(text=str(temp) + "°C")
        per_label1.config(text=str(data["main"]["pressure"]) + " hPa")

        if temp > 30:
            show_alert("⚠️ TEMPERATURE ALERT!", f"Temperature exceeded 30°C limit!\nCurrent: {temp}°C", temp)
    except Exception as e:
        w_label1.config(text="Error")
        wb_label1.config(text=str(e).capitalize())
        temp_label1.config(text="--")
        per_label1.config(text="--")

def on_button_hover(event):
    done_button.config(bg="#FF6B6B", relief="raised")

def on_button_leave(event):
    done_button.config(bg="#FF5252", relief="flat")

win = Tk()

win.title("Weather App")
win.config(bg="#1a1a2e")
win.geometry("650x650")
win.resizable(False, False)

# Heading
name_label = Label(
    win,
    text="🌤️ Weather App",
    font=("Segoe UI", 32, "bold"),
    fg="#00D4FF",
    bg="#1a1a2e"
)
name_label.place(x=25, y=30, height=60, width=600)

# Subtitle
subtitle_label = Label(
    win,
    text="Get real-time weather information",
    font=("Segoe UI", 11),
    fg="#CCCCCC",
    bg="#1a1a2e"
)
subtitle_label.place(x=25, y=95, height=25, width=600)

# State List
list_name = [ "Andhra Pradesh", "Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"
]

# City Label
city_label = Label(
    win,
    text="Select City:",
    font=("Segoe UI", 12, "bold"),
    fg="#FFFFFF",
    bg="#1a1a2e"
)
city_label.place(x=25, y=130, height=30, width=600)

# Combobox
city_name = StringVar()
style = ttk.Style()
style.theme_use('clam')
style.configure('TCombobox', fieldbackground="#2a2a3e", background="#2a2a3e", foreground="#FFFFFF")
style.map('TCombobox', fieldbackground=[('!disabled', '#2a2a3e')], foreground=[('!disabled', '#FFFFFF')])
com = ttk.Combobox(win, values=list_name,
    font=("Segoe UI", 12, "bold"), textvariable=city_name, state="normal")
com.configure(foreground="#FFFFFF")
com.place(x=25, y=165, height=45, width=600)

# Done Button
done_button = Button(
    win,
    text="Get Weather",
    font=("Segoe UI", 13, "bold"),
    fg="white",
    bg="#FF5252",
    command=get_weather,
    relief="flat",
    cursor="hand2",
    activebackground="#FF6B6B",
    activeforeground="white"
)
done_button.place(x=225, y=225, height=50, width=200)
done_button.bind("<Enter>", on_button_hover)
done_button.bind("<Leave>", on_button_leave)

# Results Frame Background
results_frame = Label(
    win,
    bg="#16213e",
    relief="flat"
)
results_frame.place(x=15, y=300, height=320, width=620)

# Weather Climate Label
w_label = Label( win, text="☁️ Weather",
    font=("Segoe UI", 11, "bold"), fg="#00D4FF", bg="#1a1a2e")
w_label.place(x=35, y=320, height=40, width=200)

w_label1 = Label(win,text="--",
    font=("Segoe UI", 14, "bold"), fg="#FFFFFF", bg="#2a2a3e", relief="flat")
w_label1.place(x=400, y=320, height=40, width=200)

# Weather Description Label
wb_label = Label(win,text="📝 Description",
    font=("Segoe UI", 11, "bold"), fg="#00D4FF", bg="#1a1a2e")
wb_label.place(x=35, y=375, height=40, width=200)

wb_label1 = Label( win, text="--",
    font=("Segoe UI", 12, "bold"), fg="#FFFFFF", bg="#2a2a3e", relief="flat")
wb_label1.place(x=400, y=375, height=40, width=200)

# Temperature Label
temp_label = Label( win,text="🌡️ Temperature",
    font=("Segoe UI", 11, "bold"), fg="#00D4FF", bg="#1a1a2e")
temp_label.place(x=35, y=430, height=40, width=200)

temp_label1 = Label(win,text="--",
    font=("Segoe UI", 14, "bold"), fg="#FFFFFF", bg="#2a2a3e", relief="flat")
temp_label1.place(x=400, y=430, height=40, width=200)

# Pressure Label
per_label = Label(win,text="🔽 Pressure",
    font=("Segoe UI", 11, "bold"), fg="#00D4FF", bg="#1a1a2e")
per_label.place(x=35, y=485, height=40, width=200)

# Pressure Value Label
per_label1 = Label( win, text="--",
    font=("Segoe UI", 12, "bold"), fg="#FFFFFF", bg="#2a2a3e", relief="flat"
)
per_label1.place(x=400, y=485, height=40, width=200)

win.mainloop()
