import requests, json
import os
from dotenv import load_dotenv

def calc(c, d):

    api = "http://api.weatherapi.com/v1"
    load_dotenv("s.env")

    access_key = os.getenv("AK")
    global mydict
    city = c
    data = d

    if data in ("current", "current weather", "current weather data"):
        mydict = {
            "access_key" : access_key,
            "query" : city
        }

        try:
            url = "{}/{}?{}&{}".format(api, "current.json", "key=" + mydict["access_key"], "q=" + mydict["query"])

            r = requests.get(url)

            with open("w.json", "w") as file:
                json.dump(r.json(), file, indent=2)

            return r

        except TypeError:
            print("Something went wrong inside if condition")

    elif data in ("3", "3 Day", "3 day", "forecast", "Forecast", "3 day forecast", "3 Day Forecast"):
        mydict = {
            "access_key" : access_key,
            "query" : city,
            "days" : 3
        }

        try:
            url = "{}/{}?{}&{}&{}".format(api, "forecast.json", "key=" + mydict["access_key"], "q=" + mydict["query"], "days=" + str(mydict["days"]))        

            r = requests.get(url)

            with open("w.json", "w") as file:
                json.dump(r.json(), file, indent=2)

            return r

        except:
            print("Something went wrong inside else condition")


if __name__ == "__main__":
    calc()
