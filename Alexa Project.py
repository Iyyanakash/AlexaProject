import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
#pyaudio
#pywhatkit
#pyjokes
#wikipedia
#openweatherapi

listener = sr.Recognizer()

engine =pyttsx3.init()
engine.say("I am your bot")
engine.say("How can i help you?")
engine.runAndWait()

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    

    
def user_commands():
    try:
        with sr.Microphone() as source:
            print("StART SPEAKING!!")
            voice=listener.listen(source)
            command =listener.recognize_google(voice)
            command =command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except Exception as e:
        print(f"There was an exception: {e}")
    return command
    
def run_alexa():
    command =user_commands()
    if 'play' in command:
        song=command.replace('play','')
        #print("New command is"+song)
        #print("The bot is telling us: Playing "+song)
        engine_talk('Playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime(('%I:%M %p'))
        engine_talk("The current time is :"+time)
        print("The current time is :"+time)
    elif 'who is' in command:
        name=command.replace('who is','')
        info = wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
    
    elif 'joke' in command:
        joke=engine_talk(pyjokes.get_joke())
        print(joke)
    
    elif 'stop' in command:
        engine_talk("Bye Bye")
        sys.exit()
    else:
        engine_talk("I could not hear you properly")
while True:
    run_alexa()
