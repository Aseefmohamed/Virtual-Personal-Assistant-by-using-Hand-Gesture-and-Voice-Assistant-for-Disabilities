import openai
import tkinter as tk
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate', 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

openai.api_key = "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"

def generate_response():
    
    prompt = query.get()
    
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=2000)
    answer = response["choices"][0]["text"]
    speak(answer)
    answer_label.config(text=answer)
    

root = tk.Tk()
root.title("ASK ME ANYTHING")

# create query entry widget
query = tk.Entry(root, width=50, font=("Helvetica", 14))
query.pack(pady=10)

# create generate button
generate_button = tk.Button(root, text="SEARCH", command=generate_response)
generate_button.pack(pady=10)

# create answer label
answer_label = tk.Label(root, text="", font=("Helvetica", 14))
answer_label.pack(pady=10)

root.mainloop()

