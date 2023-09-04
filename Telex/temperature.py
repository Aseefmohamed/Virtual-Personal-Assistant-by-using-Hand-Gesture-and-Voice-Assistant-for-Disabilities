import requests
from bs4 import BeautifulSoup
import tkinter as tk
import pyttsx3 
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def get_temperature():
    
    city = city_entry.get().lower()
    url = f"https://www.google.com/search?q=temperature+{city}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    temp = soup.find("div", class_="BNeawe").text
    temp = temp.split(":")[-1].split()[0]
    text=f"The temperature in {city} is {temp}."
    
    result_label.config(text=f"The temperature in {city} is {temp}.")
    speak(text)
    
speak("Enter the city name in the label")
# create the GUI window
window = tk.Tk()
window.title("Temperature Retrieval")

# create the input label and entry widget for city
city_label = tk.Label(window, text="Enter city:")
city_entry = tk.Entry(window)
city_label.pack()
city_entry.pack()

# create the button widget to retrieve temperature
temp_button = tk.Button(window, text="Get Temperature", command=get_temperature)
temp_button.pack()

# create the label widget to display the temperature result
result_label = tk.Label(window, text="")
result_label.pack()

# start the GUI window
window.mainloop()
