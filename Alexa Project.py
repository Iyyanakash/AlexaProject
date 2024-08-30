
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.say("I am your bot")
engine.say("How can I help you?")
engine.runAndWait()

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

def user_commands():
    command = input("Please enter your command: ").lower()
    if 'alexa' in command:
        command = command.replace('alexa', '').strip()
    return command

def run_alexa():
    command = user_commands()

    if 'play' in command:
        song = command.replace('play', '').strip()
        engine_talk('Playing ' + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk("The current time is: " + time)
    
    elif 'who is' in command:
        name = command.replace('who is', '').strip()
        info = wikipedia.summary(name, 1)
        print(info)
        engine_talk(info)
    
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
    
    elif 'stop' in command:
        engine_talk("Goodbye!")
        sys.exit()
    
    else:
        engine_talk("I could not understand your command. Please try again.")

def main():
    while True:
        run_alexa()

if __name__ == "__main__":
    main()

   




  
