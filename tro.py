from urllib import response

import requests
import speech_recognition as sr 
import webbrowser
import pyttsx3
import time
import subprocess   
import os
import tkinter as tk
import threading
from musiclibrary import MusicLibrary
from sys import path
from sites import sites
from apps import Apps
music=MusicLibrary("songs.txt")
recognizer= sr.Recognizer()
app_controller = Apps() 
def open_apps():            
      os.startfile("C:\\Users\\tiwar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
      webbrowser.open("https://youtu.be/VTLCoHnyACE?si=h01uZcaI0wglb1yg")
def countdown(minutes):
    seconds = minutes * 60

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("\nTime's up!")
    speak("Time is up. Take a break.")


# ------------------ TIMER THREAD ------------------
def start_timer(minutes=25):
    t = threading.Thread(target=countdown, args=(minutes,))
    t.daemon = True
    t.start()


# ------------------ GUI CLOCK (OPTIONAL) ------------------
def start_timer_gui(minutes=25):
    seconds = minutes * 60

    root = tk.Tk()
    root.title("Study Timer")
    root.geometry("200x100+1000+50")
    root.attributes("-topmost", True)

    label = tk.Label(root, font=("Arial", 30))
    label.pack()

    def update_timer(sec):
        if sec >= 0:
            mins, secs = divmod(sec, 60)
            label.config(text=f"{mins:02d}:{secs:02d}")
            root.after(1000, update_timer, sec - 1)
        else:
            speak("Time is up. Take a break.")

    update_timer(seconds)
    root.mainloop()
# ------------------ LLM ------------------
MODEL = "llama3"

def ask_llm(prompt):
    url = "http://localhost:11434/api/generate"
    try:
        response = requests.post(url, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        })
        return response.json()["response"]
    except:
        return "Ollama is not running. Please start it using ollama run llama3"
def startstudymode():
    speak("Study mode activated")

    open_apps()
    
    start_timer(25)
def speak(text):
 engine=pyttsx3.init()
 engine.setProperty('rate', 170)
 engine.setProperty('volume', 1.0)  
 engine.say(text)
 engine.runAndWait()
def pcommands(command):
    command = command.lower().strip()

    for name, url in sites.items():
        if name in command:
            print(f"Opening {name}")
            webbrowser.open(url)
            return True

    if "study mode" in command:
        speak("Entering study mode. I will not disturb you until you say 'exit study mode'.")
        startstudymode()
        # ---- MUSIC COMMANDS ----
    if command.startswith("play "):
        song_name = command.replace("play ", "",1).strip()
        link = music.play_by_name(song_name)

        if link:
            speak(f"Playing {song_name}")
            webbrowser.open(link)
        else:
            speak("Song not found")
        return   
    if "stop music" in command:
        speak("Stopping music")
        music.stop_music()
        return
    if app_controller.open_app(command, speak):
        return True
    if "exit" in command or "quit" in command:
        speak("Shutting down")
        exit()
        # -------- LLM --------
    speak("Thinking...")
    response = ask_llm(f"You are Synapse AI assistant. Answer clearly: {command}")
    print("Synapse:", response)
    speak(response)

if __name__=="__main__":
 print("================================")
 print("           SYNAPSE AI    ")
 print("================================")

 speak("System online. Awaiting your command......")
 #it will only wake after listening word "Synapse"
 #will get the audio from microphone
 command=None
 while True:
  
   with sr.Microphone() as source:
    print("   ....RECOGNIZING ALPHA....")
    speak("listening")
    
   try:
    with sr.Microphone() as source:
     print("     ....COMMAND ME....")
     recognizer.adjust_for_ambient_noise(source, duration=0.8)
     audio = recognizer.listen(source,timeout=20, phrase_time_limit=100)
    word=recognizer.recognize_google(audio)
    print ("...HEARD...",word)
    #Activating synapse (our assistant)
    if word != "activate":
            continue
    speak("activated")
      #..Accepting comand from use
    with sr.Microphone() as source:
          print ("..command ME..")
          recognizer.adjust_for_ambient_noise(source, duration=0.8)
          audio = recognizer.listen(source,timeout=10, phrase_time_limit=10)
          command=recognizer.recognize_google(audio)
    pcommands(command)
   except sr.UnknownValueError:
     print(" Sorry, I could not understand.")
   except sr.RequestError as e:
     print(" API error:", e) 