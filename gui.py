import tkinter as tk
from tkinter import StringVar, Frame
from weather import calc

class home():
    def __init__(self, master):
        self.master = master
        self.city = StringVar()
        self.data = StringVar()
        self.header = StringVar()
        self.weather = StringVar()
        self.date1 = StringVar()
        self.date2 = StringVar()
        self.date3 = StringVar()
        self.info1 = StringVar()
        self.info2 = StringVar()
        self.info3 = StringVar()

        label1 = tk.Label(master, text="Welcome to the Weather App", font=("Helvetica", 30), fg="blue", pady=20)
        label2 = tk.Label(master, font=("Helvetiva", 15), text="City")
        entry1 = tk.Entry(master, textvariable=self.city)
        label3 = tk.Label(master, font=("Helvetiva", 15), text="Current Weather or 3 Day Forecast")
        entry2 = tk.Entry(master, textvariable=self.data)
        label4 = tk.Label(master)
        button = tk.Button(master, font=("Helvetica", 15), text="Ok, Let's Get It!", pady=5, command=self.func)

        label1.pack()
        label2.pack()
        entry1.pack()
        label3.pack()
        entry2.pack()
        label4.pack()
        button.pack()


    def func(self):
        if self.data.get() in ("current", "current weather", "current weather data"):
            self.clear()

            req = calc(self.city.get(), self.data.get()).json()

            frame = Frame(master)
            frame.place(x=300, y=275)

            self.label5 = tk.Label(frame, textvariable=self.header, font=("Helvetica", 15))
            self.label6 = tk.Label(frame, font=("Helvetica", 13), textvariable=self.weather)

            self.label5.pack()
            self.label6.pack()

            self.header.set(req["location"]["name"] + " Current Forecast")
            self.weather.set("Temp is " + str(req["current"]["temp_f"]) + " F")


        elif self.data.get() in ("3", "3 Day", "3 day", "forecast", "Forecast", "3 day forecast", "3 Day Forecast"):
            self.clear()

            req = calc(self.city.get(), self.data.get()).json()

            frame = Frame(master)
            frame.place(x=175, y=250)

            text1 = tk.Label(frame, textvariable=self.date1, font=("Helvetica", 15), pady=20)
            text2 = tk.Label(frame, textvariable=self.date2, font=("Helvetica", 15), pady=20)
            text3 = tk.Label(frame, textvariable=self.date3, font=("Helvetica", 15), pady=20)
            info1 = tk.Label(frame, textvariable=self.info1, font=("Helvetica", 12))
            info2 = tk.Label(frame, textvariable=self.info2, font=("Helvetica", 12))
            info3 = tk.Label(frame, textvariable=self.info3, font=("Helvetica", 12))

            text1.grid(row=0, column=0, padx=20)
            text2.grid(row=0, column=1, padx=20)
            text3.grid(row=0, column=2, padx=20)
            info1.grid(row=1, column=0)
            info2.grid(row=1, column=1)
            info3.grid(row=1, column=2)

            self.date1.set(req["forecast"]["forecastday"][0]["date"])
            self.date2.set(req["forecast"]["forecastday"][1]["date"])
            self.date3.set(req["forecast"]["forecastday"][2]["date"])
            self.info1.set(
                req["forecast"]["forecastday"][0]["day"]["condition"]["text"] + "\n"
                "Max Temp: " + str(req["forecast"]["forecastday"][0]["day"]["maxtemp_f"]) + " F\n"
                "Min Temp: " + str(req["forecast"]["forecastday"][0]["day"]["mintemp_f"]) + " F" + "\n"
                "Sunrise at " + req["forecast"]["forecastday"][0]["astro"]["sunrise"] + "\n"
                "Sunset at " + req["forecast"]["forecastday"][0]["astro"]["sunset"] + "\n"
            )
            self.info2.set(
                req["forecast"]["forecastday"][1]["day"]["condition"]["text"] + "\n"
                "Max Temp: " + str(req["forecast"]["forecastday"][1]["day"]["maxtemp_f"]) + " F\n"
                "Min Temp: " + str(req["forecast"]["forecastday"][1]["day"]["mintemp_f"]) + " F" + "\n"
                "Sunrise at " + req["forecast"]["forecastday"][1]["astro"]["sunrise"] + "\n"
                "Sunset at " + req["forecast"]["forecastday"][1]["astro"]["sunset"]
            )
            self.info3.set(
                req["forecast"]["forecastday"][2]["day"]["condition"]["text"] + "\n"
                "Max Temp: " + str(req["forecast"]["forecastday"][2]["day"]["maxtemp_f"]) + " F\n"
                "Min Temp: " + str(req["forecast"]["forecastday"][2]["day"]["mintemp_f"]) + " F" + "\n"
                "Sunrise at " + req["forecast"]["forecastday"][2]["astro"]["sunrise"] + "\n"
                "Sunset at " + req["forecast"]["forecastday"][2]["astro"]["sunset"] + "\n"
            )

        
    def clear(self):
        self.header.set("")
        self.weather.set("")
        self.date1.set("")
        self.date2.set("")
        self.date3.set("")
        self.info1.set("")
        self.info2.set("")
        self.info3.set("")


def main():
    global master
    master = tk.Tk()
    master.geometry("800x500")
    Home = home(master)
    master.mainloop()



if __name__ == "__main__":
    main()