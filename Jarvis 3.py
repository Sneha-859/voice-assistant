import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine= pyttsx3.init('sapi5')
voices = engine. getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',  voices[0].id)



def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis, how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio= r.listen(source)

    try:

        print("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said:{query}\n")
        
    except Exception as e:
        print(e)

        print("Say that again please......")
        return "None"

    return query





if __name__ == "__main__":
    wishMe()
    while True:
       query = takeCommand().lower()

       if 'wikipedia' in query:
        speak("Searching Wikipedia.......")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

       elif 'open youtube' in query:
        webbrowser.open("youtube.com")

       elif 'open coding ninjas' in query:
        webbrowser.open("classroom.codingninjas.com")
        
       elif 'open google' in query:
        webbrowser.open("google.com")

       elif 'open codechef' in query:
        webbrowser.open("www.codechef.com")

       elif 'open maps' in query:
        webbrowser.open("maps.google.com")


       elif 'open gmail' in query:
        webbrowser.open("gmail.com")

       elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

       elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

       elif "open game" in query:
        gamePath= "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
        os.startfile(gamePath)

       elif "open code" in query:
         codePath= "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath)

       elif "open brave" in query:
         bravePath= "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
         os.startfile(bravePath)

       if "quit" in query:
        exit()


       