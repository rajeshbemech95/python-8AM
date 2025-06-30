# from  gtts import gTTS
# import speech_recognition as sr
# # text = "hello i am there"
# # language = "en"

# # speech = gTTS(text=text, lang=language,slow=False)
# # speech.save("audio.mp3")

# reg = sr.Recognizer()
# with sr.AudioFile('audio.wav') as source:
#     audio = reg.record(source)
#     text = reg.recognize_bing(audio)
#     print("text :",text)

# api.openweathermap.org/data/2.5/weather

import requests
import tkinter as tk
from tkinter import messagebox

# api_key = "6ccd9dd61998c046786e91840a77ee56"
# city = "chennai"
# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# response = requests.get(url)
# data = response.json()
# print("respose status",response)
# print(data)


def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input require", "enter city")
        return
    
    api_key = "6ccd9dd61998c046786e91840a77ee56"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data=response.json()
            
            result = (
                f"City: {data["name"], data["sys"]['country']}\n"
                f"Temp: {data["main"]["temp"]}C\n"
            )
            res_lable.config(text=result)
            
        else:
            messagebox.showerror("Error","API key or city not found")
            
    except requests.RequestException as e:
        messagebox.showerror("Error",e)
        
        
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False,False)

tk.Label(root,text="Enter the city name").pack()
city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root,text="Get Weather",command=get_weather).pack()
res_lable = tk.Label(root,text="Current data")
res_lable.pack()
root.mainloop()