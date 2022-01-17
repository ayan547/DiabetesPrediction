import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#adding the male voice
engine.setProperty('voice', voices[0].id)
#speed of speech
engine. setProperty("rate", 190)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!.....Ayan")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!....Ayan")

    else:
        speak("Good Evening!....Ayan")

    speak("I am Modi ...............and i am the ruler of India. Please tell me how may I help you")

def takeCommand():
    #takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.9
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        if 'Modi close' in query:
            speak("Goodbye")
            exit()

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
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
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in query:
            music_dir = "C:\\Users\\KIIT\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(music_dir)

        elif 'play chess' in query:
            webbrowser.open("https://www.chess.com/home#")

        elif 'play valorant' in query:
            val_dir = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(val_dir)





