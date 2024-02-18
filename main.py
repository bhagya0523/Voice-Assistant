import ctypes
import datetime
import os
import shutil
import webbrowser
import pyjokes
import pyttsx3  # text to speech
import pywhatkit
import speech_recognition as sr
import wikipedia
import wolframalpha

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 180)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")
        print("Good Afternoon !")

    else:
        speak("Good Evening !")
        print("Good Evening !")

    print("I am your voice assistant Leesa")
    assname = "leesa"
    speak("I am your voice assistant")
    speak(assname)


def callName():
    speak("How should i address you")
    uname = takeCommand()
    speak("Welcome to the voice assistant")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print(
        "-------------------------------------------------------------------".center(
            columns
        )
    )
    print("Welcome ", uname.center(columns))
    print(
        "---------------------------------------------------------------------".center(
            columns
        )
    )

    speak("How can i Help you")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == "__main__":
    clear = lambda: os.system("cls")  # clear cmd prompt

    clear()
    greet()
    callName()


while True:
    query = takeCommand().lower()

    if "who are you" in query:
        speak("I am your virtual assistant leesa")

    elif "who i am" in query:
        speak("you are a human.")

    elif "how are you" in query:
        speak("I am fine, Thank you")
        speak("How are you")

    elif (
        "fine" in query or "good" in query or "great" in query or "doing well" in query
    ):
        speak("It's good to know that your fine")
        speak("How can i Help you")

    elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "open youtube" in query:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    elif "open google" in query:
        speak("Here you go to Google\n")
        webbrowser.open("google.com")

    elif "play" in query:
        any = query.replace("play", "")
        speak(f"Playing {any}")
        pywhatkit.playonyt(any)

    elif "play music" in query or "play song" in query:
        speak("Here you go with music")
        query = query.replace("play", "")
        speak(f"Playing {query}")
        pywhatkit.playonyt(query)

    elif "what is the time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(current_time)
        speak(f"The current time is {current_time}")

    elif "exit" in query:
        speak("Thanks for giving me your time")
        speak("Goodbye")
        exit()

    elif "joke" in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    elif "calculate" in query:
        app_id = "YJHX7J-JLRW3V2KLU"
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index("calculate")
        query = query.split()[indx + 1 :]
        res = client.query(" ".join(query))
        answer = next(res.results).text
        print("The answer is " + answer)
        speak("The answer is " + answer)

    elif "search" in query or "play" in query:
        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.open(query)

    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        speak("You asked to Location")
        info = wikipedia.summary(location, sentences=1)
        print(info)
        speak(info)

    elif "who is" in query:
        person = query.replace("who is", "")
        info = wikipedia.summary(person, sentences=1)
        print(info)
        speak(info)

    elif "what is" in query:
        thing = query.replace("what is", "")
        info = wikipedia.summary(thing, sentences=1)
        print(info)
        speak(info)

    elif "why" in query or "how to " in query:
        query = query.replace("why", "")
        webbrowser.open(query)

    elif "lock window" in query:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()
