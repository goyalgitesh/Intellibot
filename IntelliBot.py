import pyttsx3
import datetime as dt
import speech_recognition as sr
import wikipedia as wk
import smtplib as sp
import webbrowser as wb
import os
import pyautogui as pi

engine = pyttsx3.init()
engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = dt.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


def date():
    year = int(dt.datetime.now().year)
    month = int(dt.datetime.now().month)
    day = int(dt.datetime.now().day)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)

def play_songs():
     songs_dir = r"C:\Users\DELL\Downloads\Music"
     songs = os.listdir(songs_dir)
     os.startfile(os.path.join(songs_dir,songs[0]))

def remember_that():
    speak("What should I remember?")
    data = takeCommand()
    speak("you saide me to remember that "+data)
    remember = open('data.txt','w')
    remember.write(data)
    remember.close()
    return remember

def know(remember):
    remember.open('data.txt','r')
    speak("you said me to remember that" + remember.read())


def wishme():
    hour = dt.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    elif hour > 12 and hour <= 18:
        speak("Good Afternoon Sir!")
    elif hour > 18 and hour <= 21:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("Welcome back!")
    time()
    date()
    speak("Intellibot is always here to help you Sir!")
    speak("Please tell me how can I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please....")
        return "None"

    return query


def sendEmail(to, content):
    server = sp.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('goyalg1017@gmail.com', 'Goyal$1789')
    server.sendmail("goyalg1017@gmail.com", to, content)
    server.close()

def sshot():
    img = pi.screenshot()
    img.save(r"D:\\College\\IntelliBot\\ss.png")


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'im00invisible@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Unable to send the email")


        elif 'wikipedia' in query:
            speak("Searching.....Please Wait")
            query = query.replace("wikipedia", "")
            result = wk.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'chrome' in query:
            speak("What should I search ?")
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chrome_path).open_new_tab(search + '.com')

        

        
        #elif 'screenshot' or 'screen shot' in query:
            #sshot()
            #speak("The ScreenShot is taken successgully and saved to Camera Roll.")

       # elif 'remember that' or 'remember' in query:
         #   remember_that()
         #   memory = remember_that()

      #  elif 'do you know anything' or 'know' in query:
         #   know(memory)

        #elif 'play songs' or 'play music' in query:
            #play_songs()

       




        elif 'logout' or 'log out' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")



        elif 'offline' or 'quit' or 'exit' in query:
            speak("See you again soon Sir")
            speak("Intellibot is now turned off")
            quit()
