import speech_recognition as sr 
import webbrowser
import pyttsx3
import time
from musiclibrary import MusicLibrary
recognizer= sr.Recognizer()
def speak(text):
 engine=pyttsx3.init()
 engine.setProperty('rate', 170)
 engine.setProperty('volume', 1.0)  
 engine.say(text)
 engine.runAndWait()
sites = [
    ["youtube", "https://www.youtube.com"],
    ["wikipedia", "https://www.wikipedia.org"],
    ["google", "https://www.google.com"],
    ["github", "https://github.com"],
    ["stackoverflow", "https://stackoverflow.com"],
    ["linkedin", "https://www.linkedin.com"],
    ["instagram", "https://www.instagram.com"],
    ["facebook", "https://www.facebook.com"],
    ["twitter", "https://twitter.com"],
    ["reddit", "https://www.reddit.com"],
    ["amazon", "https://www.amazon.in"],
    ["flipkart", "https://www.flipkart.com"],
    ["netflix", "https://www.netflix.com"],
    ["spotify", "https://www.spotify.com"],
    ["chatgpt", "https://chat.openai.com"]
]
music=MusicLibrary("songs.txt")
def pcommands(command):
    command = command.lower().strip()

    for site in sites:
        if site[0] in command:
            speak(f"Opening {site[0]}")
            webbrowser.open(site[1])
            return
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
    if "exit" in command or "quit" in command:
        speak("Shutting down")
        exit()
    
    speak("Sorry, I didn't understand that")

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
