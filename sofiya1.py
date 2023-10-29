import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak(" I am Sofiya Sir  Please tell me how may I help you.")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  
        audio = r.listen(source, timeout=10)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query

    except Exception as e:
        print(e)
        print("Say that again, please...")
        return "None"

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        
         #logoic base in commands.
        if "open youtube" in query:
             webbrowser.open("https://youtube.com/")

        elif "open google " in query:
            webbrowser.open("https://www.google.com/")

        elif "open bookmyshow" in query:
            webbrowser.open("https://in.bookmyshow.com/")
        
        elif "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "play music" in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            random_index = random.randint(0, len(songs) - 1)
            random_song = songs[random_index]
            print("Playing song:", random_song)
            os.startfile(os.path.join(music_dir, random_song))

        elif "bye" in query:
            speak("goodbye sir have a nice day sir!")
            break 