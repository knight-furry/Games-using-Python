import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        print("Good morning sir !")
        speak("Good morning sir !")
    elif hour >= 12 and hour < 18:
        print("Good afternoon sir !")
        speak("Good afternoon sir !")
    else:
        print("Good evening sir !")
        speak("Good evening sir !")
    print("I am Rashmika. Please tell me how may I help you....")
    speak("I am Rashmika. Please tell me how may I help you....")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        quary = r.recognize_google(audio, language='en-in')
        print("User said : ", quary)
    except Exception as e:
        # print(e)
        speak("Say that again please.....")
        print("Say that again please.....")
        return "None"
    return quary


if __name__ == '__main__':
    wishme()
    while True:
        quary = takecommand().lower()

        if 'wikipedia' in quary:
            speak("Searching wikipedia.....")
            quary = quary.replace("wikipedia", "")
            results = wikipedia.summary(quary, sentences=2)
            speak("According to wikipedia.....")
            print(results)
            speak(results)

        elif 'open youtube' in quary:
            webbrowser.open("youtube.com")

        elif 'open google' in quary:
            webbrowser.open("google.com")

        elif "love you" in quary:
            print("Ok sir as your wish. thank you so much.....")
            speak("Ok sir as your wish. thank you so much.....")
            break

        elif "play music" in quary:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            # print(songs)
            num = random.randrange(0, 100)
            os.startfile(os.path.join(music_dir, songs[num]))

        elif 'the time' in quary:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The running time is")
            speak(strTime)

        elif "can you hear me" in quary:
            speak("Yes sir I can hear you. Tell me what can I help you")
