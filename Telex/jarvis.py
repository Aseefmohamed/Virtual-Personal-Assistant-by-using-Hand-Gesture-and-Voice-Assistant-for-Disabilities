import pyttsx3
import speech_recognition as sr
import datetime
import os
import openai
import wikipedia
import subprocess
import pywhatkit
import requests
from bs4 import BeautifulSoup
from pyautogui import moveTo,write,leftClick
import pyjokes
import webbrowser
import pyautogui
import datetime
import colorama
from colorama import Fore
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer,QTime,QDate
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from jarvisSuperUI import Ui_Form


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


     
    
     
def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

class MainThread(QThread):
    def __init__(self):
        
        super(MainThread,self).__init__()
    
    def run(self):
        self.TaskExection()

    def commands(self):
     
        r = sr.Recognizer()
        with sr.Microphone() as source:
            
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source , duration=1)
            audio=r.listen(source)
        try:
            
            query = r.recognize_google(audio, language='en-in')
            print(f"You Just Said: {query}\n")
        except Exception as e:
            print(e)
            
            query="none"
        
        return query
      

    def wishings(self):
        hour = int(datetime.datetime.now().hour)
        if hour >=0 and hour<12:
            
            speak('Good morning BOSS')
        elif hour>=12 and hour<17:
            
            speak("Good Afternoon BOSS")
        elif hour >=17 and hour<21:
            
            speak("Good Evening BOSS")
        else:
            
            speak("Good Night BOSS")


    def TaskExection(self):
        
        def open_another_file(self):
         
            speak('you switched to hand sign mode')
            os.startfile("hand_assistant.py")
            
        self.wishings()
        while True:
            self.query = self.commands().lower()
            if 'time' in self.query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak("Sir, The time is: " + strTime)
                    print(strTime)
            elif 'question' in self.query or 'doubts' in self.query or 'question' in self.query or 'doubt' in self.query:
                    openai.api_key = "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"
                    speak('ask anything')
                    prompt = self.commands().lower()
                    if prompt in "none":
                       continue
                    print("Your query:", prompt)
                    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=2000)
                    a= response["choices"][0]["text"]
                    print(a)
                    speak(a)

            elif 'wikipedia' in self.query:
                speak("Searching in wikipedia")
                try:
                    self.query=self.query.replace("wikipedia", '')
                    results = wikipedia.summary(self.query, sentences=1)
                    speak("According to Wikipedia..")
                    print(results)
                    speak(results)
                except:
                    print("No results found..")
                    speak("no results found")

            elif 'play' in self.query:
                playquery=self.query.replace('play','')
                speak("Playing " + playquery)
                pywhatkit.playonyt(playquery)
            elif 'gmail' in self.query:
                speak('Opening Gmail....')
                url = "https://www.gmail.com"
                webbrowser.open_new_tab(url)
            elif 'youtube' in self.query:
                speak('Opening....')
                url = "https://www.youtube.com"
                webbrowser.open_new_tab(url)
            elif 'music' in self.query:
                speak('Playing')
                music_dir = 'fav songs'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))       
                 
            elif 'temperature' in self.query:
                 speak('sure, Tell me the city')
                 print("Tell me the city")
                 city = self.commands().lower()
                 print(city)
                 url = f"https://www.google.com/search?q=temperature+{city}"
                 r = requests.get(url)
                 soup = BeautifulSoup(r.text, "html.parser")
                 temp = soup.find("div", class_="BNeawe").text
                 temp = temp.split(":")[-1].split()[0]
                 z= f"The temperature in {city} is {temp}."
                 print(z)
                 speak(z)
                 continue
            

            elif 'screenshot ' in self.query:
                 now = datetime.datetime.now()
                 filename = "screenshot{}.png".format(now.strftime("%Y-%m-%d-%H-%M-%S"))
                 pyautogui.screenshot(filename)

 


            elif 'joke' in self.query:
                jarvisJoke = pyjokes.get_joke()
                print(jarvisJoke)
                speak(jarvisJoke)
            else:
                speak("please say the command again")

def open_another_file():
         
         speak('you switched to hand sign mode')
         
         os.startfile("hand_assistant.py")
         
         
            

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.startPushButton.clicked.connect(self.startTask)
        self.ui.quitPushButton.clicked.connect(open_another_file)

    def startTask(self, text):
        self.ui.movie = QtGui.QMovie("GUI files\\telex.gif")
        self.ui.ironManBackground.setMovie(self.ui.movie)
        self.ui.movie.start()
        # ironmanGIF
        self.ui.movie = QtGui.QMovie("GUI files\\listeningGIF.gif")
        self.ui.ironManGIF.setMovie(self.ui.movie)
        self.ui.movie.start()
        # dateLabel
        self.ui.movie = QtGui.QMovie("GUI files\\gggf.jpg")
        self.ui.dateLabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        # timeLabel
        self.ui.movie = QtGui.QMovie("GUI files\\gggf.jpg")
        self.ui.timeLabel.setMovie(self.ui.movie)
        self.ui.movie.start()
        # startLabelNotButton
        self.ui.movie = QtGui.QMovie("GUI files\\20230401_185949_0000.png")
        self.ui.startLabelNotButton.setMovie(self.ui.movie)
        self.ui.movie.start()
        # quitLabelNotButton
        self.ui.movie = QtGui.QMovie("GUI files\\20230401_191740_0000.png")
        self.ui.quitLabelNotButton.setMovie(self.ui.movie)
        self.ui.movie.start()
        # earthGIF
        self.ui.movie = QtGui.QMovie("GUI files\\Earth.gif")
        self.ui.earthGIF.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        currentTime = QTime.currentTime()
        currentDate = QDate.currentDate()
        labelTime = currentTime.toString('hh:mm:ss')
        labelDate = currentDate.toString(Qt.ISODate)
        self.ui.dateTextBrowser.setText(f"Date: {labelDate}")
        self.ui.timeTextBrowser.setText(f"Date: {labelTime}")
    

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
