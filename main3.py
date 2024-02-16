import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
import subprocess
import time
import pyjokes
import cohere
from api import cohere_api
import smtplib
from confidential import your_email
from confidential import password

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 < hour < 12:
        speak("Good Morning Sir!")
    elif 12 < hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Brad, your personal assistant. How may I help you!")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(your_email, password)
    server.sendmail(your_email, to, content)
    server.close()

# convert audio to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            print("Recognising...")
            text = r.recognize_google(audio, language='en-in')
            print(text)
        except Exception:  # error handling
            speak("")
            return "None"
        return text
chatStr = ""
def chat(query):
    global chatStr
    co = cohere.Client(cohere_api)
    chatStr += f"Navnit: {query}\n Brad: "
    # generate a prediction for a prompt
    response = co.generate(
        model='command-nightly',
        prompt=chatStr,
        max_tokens=300,
        temperature=0.9,
        stop_sequences=[],
        return_likelihoods='NONE')
    speak('{}'.format(response.generations[0].text))
    chatStr += f"{format(response.generations[0].text)}\n"
    return format(response.generations[0].text)
# for main function
if __name__ == '__main__':
    wish()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(5)
        elif "open a website" in query:
            speak("What website do you want to open?")
            website = takeCommand()
            webbrowser.open(website)
            speak("Opening " + website)
            time.sleep(5)
        elif "send email" in query:
            try:
                speak("Who do you want to send email to? Please type the email id")
                email_id = input()
                to = email_id
                speak("What should I say in the mail?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I couldn't send this email. Please try again, Thank You.")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            time.sleep(5)
        elif "google" in query or "open web browser" in query:
            webbrowser.open("www.google.com")
            speak("Opening Google...")
            time.sleep(5)
        elif "gmail" in query:
            webbrowser.open("www.gmail.com")
            speak("Opening Gmail...")
            time.sleep(5)
        elif "youtube" in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("Opening Youtube...")
            time.sleep(5)
        elif "news" in query:
            webbrowser.open("www.timesofindia.indiatimes.com")
            speak("Here's some latest news for you...")
            time.sleep(5)
        elif "cricket" in query:
            webbrowser.open("www.cricbuzz.com")
            speak("Some Hot Cricket is right here on your screen...")
            time.sleep(5)
        elif "joke" in query:
            speak(pyjokes.get_joke())
            time.sleep(5)
        elif "netflix" in query:
            webbrowser.open("www.netflix.com")
            speak("Opening Netflix...")
            time.sleep(5)
        elif "prime video" in query or "prime" in query:
            webbrowser.open("www.primevideo.com")
            speak("Opening Prime Video...")
            time.sleep(5)
        elif "bookmyshow" in query:
            webbrowser.open("https://in.bookmyshow.com/")
            speak("Opening BookMyShow...")
            time.sleep(5)
        elif "pycharm" in query:
            subprocess.call(['C:\Program Files\JetBrains\PyCharm Community Edition 2023.3.2\\bin\pycharm64.exe'])
            speak("Opening Pycharm...")
            time.sleep(5)
        elif "irctc" in query:
            webbrowser.open("www.irctc.in")
            speak("Opening I R C T C...")
            time.sleep(5)
        elif "amazon" in query:
            webbrowser.open("www.amazon.in")
            speak("Opening Amazon India...")
            time.sleep(5)
        elif "redbus" in query:
            webbrowser.open("www.redbus.in")
            speak("Opening RedBus...")
            time.sleep(5)
        elif "flipkart" in query:
            webbrowser.open("www.flipkart.com")
            speak("Opening Flipkart...")
            time.sleep(5)
        elif "spotify" in query:
            webbrowser.open("www.spotify.com")
            speak("Opening Spotify...")
            time.sleep(5)
        elif "instagram" in query:
            webbrowser.open("www.instagram.com")
            speak("Opening Instagram...")
            time.sleep(5)
        elif "linkedin" in query:
            webbrowser.open("www.linkedin.com")
            speak("Opening LinkedIn...")
            time.sleep(5)
        elif "facebook" in query:
            webbrowser.open("www.facebook.com")
            speak("Opening Facebook...")
            time.sleep(5)
        elif "whatsapp" in query:
            webbrowser.open("web.whatsapp.com")
            speak("Opening Web Whatsapp...")
            time.sleep(5)
        elif "vs code" in query or "visual studio code" in query:
            subprocess.call(['C:\\Users\globa\AppData\Local\Programs\Microsoft VS Code\Code.exe'])
            speak("Opening Visual Studio Code...")
            time.sleep(5)
        elif "telegram" in query:
            webbrowser.open("web.telegram.org")
            speak("Opening Telegram...")
            time.sleep(5)
        elif "music" in query or "songs" in query:
            speak("Playing Music")
            music_dir = "D:\Bhajan"
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, musics[0]))
            time.sleep(5)
        elif "videos" in query:
            speak("Playing Videos")
            video_dir = "D:\Bhajan"
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[0]))
            time.sleep(5)
        elif "shutdown" in query:
            speak("Shutting Down...")
            os.system('shutdown -s')
            time.sleep(5)
        elif "restart" in query:
            speak("Restarting...")
            os.system('shutdown /r')
            time.sleep(5)
        elif "sleep" in query:
            speak("P C going to sleep")
            os.system('rundll32.exe powrprof.dll, SetSuspendState Sleep')
        elif "quit" in query:
            speak("Quitting. It was Nice Helping you with your work.")
            quit()
        else:
            chat(query)
