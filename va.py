import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import os



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'va' in command:
                command = command.replace('va', '')
                print(command)
    except:
        pass
    return command


def Intro():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning! How can I help you")
    elif hour>=12 and hour<18:
        talk("Good Afternoon! How can I help you")
    else:
        talk("Good Evening! How canI help you")


def run_va():

    command = take_command()
    print(command)
    if 'how are you' in command:
        talk("I am doing well, how are you today?")
    elif 'how is the family' in command:
        talk("the family is doing great, thank you")

    elif 'thank you' in command:
        talk("your welcome, have a good day!")
    elif 'open google' in command:
        webbrowser.open_new_tab("https://www.google.ca")
        talk("Google chrome is open now")
        time.sleep(2)
    elif 'open youtube' in command:
        webbrowser.open_new_tab("https://www.youtube.com")
        talk("Youtube is open now")
        time.sleep(2)
    elif 'open gmail' in command:
        webbrowser.open_new_tab("https://www.gmail.com")
        talk("Gmail is open now")
        time.sleep(2)
    elif 'canadian news' in command:
        webbrowser.open_new_tab("https://www.cbc.ca")
        webbrowser.open_new_tab("https://www.ctvnews.ca")
        time.sleep(2)
    elif 'american news' in command:
        webbrowser.open_new_tab("https://www.msnbc.com")
        webbrowser.open_new_tab("https://www.cnn.com")
        time.sleep(2)
    #elif 'search' in command:
     #   command = command.replace("search", "")
      #  webbrowser.open("https://www.google.ca", new = 2, command)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' or 'what is' in command:
        thing = command.replace('who is', '')
        info = wikipedia.summary(thing, 3)
        print(info)
        talk(info)
    elif 'open' in command:
        os.startfile("ms word")
    else:
        talk('Please say the command again.')


while True:
    Intro()
    run_va()