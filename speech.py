'''
What this AI Assistant can do for you:
1)play music
2)Take notes and store it in a text file
3)Wikipedia searches
4)capable of opening websites like Google, Youtube, etc., in a web browser.
5)capable of opening other applications with a single voice command.

'''

import pyttsx3 #text to speech conversion library
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5') #microsoft api for voice
print(type(engine))
voices = engine.getProperty('voices')
# print(voices[1].id)// 0 for male and 1 for female voice
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("How may I help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  #seconds of non speaking audio
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1: #if we want to run only once
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Twesha\\Desktop\\AI_PROJECT\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'open excel' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codePath)

        elif "note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('randomfile.txt', 'w')
            file.write(note)
         
        elif "display" in query:
            speak("Showing Notes")
            file = open("randomfile.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'bye' in query:
            speak("Thanks for giving me your time")
            exit()
          
          