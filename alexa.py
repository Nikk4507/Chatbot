import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import psutil
from datetime import date



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energi_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query


def Command():
    a = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        a.pause_threshold = 1
        a.energi_threshold = 300
        audio = a.listen(source)
    try:
        print("Recognizing...")
        query = a.recognize_google(audio, language = 'en-in')
        print(f"User said: {input}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return input


def convertTime(seconds):
    minutes,seconds = divmod(seconds , 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching in Wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("acoording to wikipedia")
            speak(results)


        elif 'hey' in query:
            speak("yes Sir!")

        elif 'hello' in query:
            speak("Hello Nikhil sir! How are your sir?")
        elif "fine" in query:
            speak("Nice to hear sir!")
        elif 'thank you' in query:
            speak("Its my pleasure sir!Have a nice day")



        elif 'date' in query:
            today = date.today()
            speak(f"today's date is {today}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir! the time is  {strTime}")

        elif 'play some music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            i = random.randint(0,15)
            os.startfile(os.path.join(music_dir, songs[i]))

        elif 'search something' in query:
            speak("What do you want to search? Please speak")
            while True:
                b = takeCommand().lower()
                webbrowser.open('https://www.google.com/search?q='+b)
                break

        # elif 'Set reminder' in query:
        #     speak("say the time")
        #     while True:
        #         c = takeCommand().lower()
        #         strTime = datetime.datetime.now().strftime("%H:%M")
        #         if strftime == c:
        #             speak("Its your reminder")
        #             break
