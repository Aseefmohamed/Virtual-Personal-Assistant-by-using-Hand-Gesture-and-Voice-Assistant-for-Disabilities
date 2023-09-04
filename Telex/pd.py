import cv2
import pyttsx3
import ctypes

# Load the pre-trained cascade classifier for eye detection
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Initialize the camera
cap = cv2.VideoCapture(0)

# Initialize the speech engine


 
while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect eyes in the grayscale image
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(20,20))

    # Draw a rectangle around each detected eye
    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the number of eyes detected in the frame
    num_eyes = len(eyes)
    cv2.putText(frame, f'Number of Eyes: {num_eyes}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Warn the user if more than one eye is detected
    if num_eyes > 3:
        import pyautogui

        pyautogui.hotkey('winleft')
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
# print(voices[0].id)
        engine.setProperty('voice', voices[0].id)  
        def speak(audio):
            engine.say(audio)
            engine.runAndWait()
        speak("Alert !! It seems like there's someone else in the room")
        
        
        # Lock the screen if the user confirms with voice command
        # ...

    # Display the resulting frame
    cv2.imshow('Eye Detection', frame)

    # Wait for a key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
