
# import necessary packages
frame_counter = 0

import cv2
import time
import subprocess 
import numpy as np
import pyttsx3
import wikipedia
import openai
import webbrowser
import pyjokes
import time
import os
import requests
import ctypes

import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import ImageGrab

import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
speak('Hii I am Telex..... You can assist me in hand sign also')
# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)


# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    #print(result)
    
    className = ''


    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                #print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)
               

                landmarks.append([lmx, lmy])
                
            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
            frame_counter += 1
            
            # Predict gesture after 3 seconds
            if frame_counter == 90:
            # Predict gesture
               prediction = model.predict([landmarks])
               classID = np.argmax(prediction)
               className = classNames[classID]
            if frame_counter == 91:
               frame_counter = 0
               className = ''

    # show the prediction on the frame
        cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, cv2.LINE_AA)

    # Show the final output
    cv2.imshow("TELEX-HAND ASSISTANT", frame )
    
    if 'peace' in className:
                    speak('Sure, I have an capabilities to detect the temperature')
                    os.startfile("temperature.py")
         
    if 'thumbs down' in className:
                    speak('ask me anything')
                    os.startfile("chatgpt.py")

    if 'live long' in className:
          speak('Opening Gmail, sign in to your account')
          url = "https://www.gmail.com"
          webbrowser.open_new_tab(url)
    
                    
    if 'thumbs up' in className:
                    speak('opening notepad')
                    notepad_path = r'C:\Windows\System32\notepad.exe'
                    subprocess.run([notepad_path])
                    
    if 'stop' in className:
                    speak('Set your alarm now')
                    speak('Enter the time of alarm to be set')
                    os.startfile("alarm.py")
                    time.sleep(5)
    if 'call me' in className:
                    speak('Playing')
                    music_dir = 'fav songs'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))
                    continue

    if 'rock' in className:
                    speak('I am going to lock the screen')
                    ctypes.windll.user32.LockWorkStation()
                    
    if 'okay' in className:
                    speak('I am going to take screenshot. keep arrange your display')
                    time.sleep(5)
                    
                    now = datetime.datetime.now()
                    filename = "screenshot{}.png".format(now.strftime("%Y-%m-%d-%H-%M-%S"))
                    pyautogui.screenshot(filename)
                    speak('screenshot taken')

    if 'smile' in className:
                    os.system('jarvisJoke = pyjokes.get_joke()')
                    print(jarvisJoke)
                    speak(jarvisJoke)
    if 'fist' in className:
                    speak('WPS office is opening. You can create ppt, word document, etc.,')
                    os.startfile("uwp_wpsoffice.exe")
                    
    if cv2.waitKey(1) == ord('q'):
                    break
    
# release the webcam and destroy all active windows
cap.release()

cv2.destroyAllWindows()

