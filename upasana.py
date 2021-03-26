import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
listener = sr.Recognizer()
talk = pyttsx3.init()
newvoicerate = 140
talk.setProperty("rate",newvoicerate)
talk.setProperty("voice", "english_rp+f3")
def sound(text):
    talk.say(text)
    talk.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if "Upasana" in command:
                command = command.replace("Upasana","")
                #c8usound(command)
                print(command)
    except:

        return command

def run_upasana():
    command = take_command()
    print(command)
    #if "Upasana" in command:

    if "play" in command:
        song = command.replace("play","")
        sound("playing" + song)
        pywhatkit.playonyt(song)
    elif "tell me about" in command:
        result = command
        info = wikipedia.summary(result ,1)
        print(info)
        sound(info)
    elif "who is" in command:
        result = command.replace("who is","")
        info = wikipedia.summary(result ,1)
        print(info)
        sound(info)
    elif "are you single" in command:
        sound("I am in relationship with Rahul")
    elif "do you love me" in command:
        felling = ("i love you rahul")
        sound(felling)
        print(felling)
    elif "time" in command:
        t = datetime.datetime.now().strftime("%I,%M,%P")
        print(t)
        sound("the current time is" +t)
    elif "date" in command:
        d = datetime.date.today()
        print(d)
        sound(d)
    elif "neha" in command:
        sound("neha ek dm kara mal hai")

    else:
        sound("hatt behnchod")

run_upasana()
