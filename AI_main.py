import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
# import python_weather
import pyjokes
import tkinter as tk
from tkinter import *



class mainClass:
    def __init__(self):

        self.engine = pyttsx3.init('sapi5')
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate-25)
        self.voices = self.engine.getProperty('voices')

        # print(voices[1].id)
        self.engine.setProperty('voice', self.voices[0].id)
        b = True
        self.wishMe()
        while True:
            # if 1:

            query = self.takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:

                self.speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                self.speak("According to Wikipedia")
                print(results)
                self.speak(results)
            elif 'play' in query:

                song = query.replace('play', '')
                self.speak('playing ' + song)
                pywhatkit.playonyt(song)

            elif 'open youtube' in query:

                webbrowser.open('https://www.youtube.com')

            elif 'open whatsapp' in query:

                webbrowser.open("https://web.whatsapp.com/");

            elif 'open google' in query:

                webbrowser.open("google.com")


            elif 'open stack overflow' in query:

                webbrowser.open("stackoverflow.com")

            elif 'play music' in query:

                music_dir = 'E:\All Latest song\All Latest song'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:

                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                self.speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:

                codePath = "E:\SEM 4\PSC\Lab\6.py"
                os.startfile(codePath)

            elif 'joke' in query:

                self.speak(pyjokes.get_joke())


            elif 'email' in query:

                try:
                    self.speak("What should I say?")
                    content = self.takeCommand()
                    to = "tptm45@gmail.com"
                    self.sendEmail(to, content)
                    self.speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    self.speak("Sorry Sir , Mail cannot be Sent!")
            elif 'quit' or 'stop' in query:
                break
    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speak("Good Morning!")

        elif hour >= 12 and hour < 18:
            self.speak("Good Afternoon!")

        else:
            self.speak("Good Evening!")

        self.speak("I am Alexa. Please tell me how may I help you")

    def takeCommand(self):
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            print(audio)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            self.speak("Say that again please...")
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()


"""
    def _init_(self,root,ls):
        wishMe()


"""