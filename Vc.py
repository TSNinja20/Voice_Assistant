import pyttsx3 as pyt #text to speech converter
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

"""speech_recognition function 
Speech/Audio to text converter"""

def sptext():
    recognizer = sr.Recognizer()#catch our word through Recognizer class
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)#noise cancellation
        audio = recognizer.listen(source)#microphone listen
        #data read
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand!")

"""Text to speech/Audio converter"""
def speechtx(x):
    engine = pyt.init()#init class use through function call
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate",150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':


    if "ninja" in sptext().lower():
        while True:       
                data1 = sptext().lower()

                if "your name" in data1:
                    name = "my name is ninja"
                    speechtx(name)

                elif "old are you" in data1:
                    age = "I'm one years old"
                    speechtx(age)

                elif "built" in data1:
                    built = "My professor built me"
                    speechtx(built)

                elif "professor" in data1:
                    pname = "My professor name is Rajib Kuri"
                    speechtx(pname)

                elif "thank you" in data1:
                    ty = "it's my pleasure"
                    speechtx(ty)


                elif "time" in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtx(time)

                elif "youtube" in data1:
                    webbrowser.open("https://www.youtube.com/")

                elif "translate" in data1:
                    webbrowser.open("https://translate.google.com/")

                elif "linkedin" in data1:
                    webbrowser.open("https://www.linkedin.com/feed/")

                elif "joke" in data1:
                    joke_1 = pyjokes.get_joke(language="en",category="neutral")
                    print(joke_1)
                    speechtx(joke_1)

                elif "play song" in data1:
                    add = "F:\Darjeeling\Darjeeling Audio"
                    listsong = os.listdir(add)
                    print(listsong)
                    os.startfile(os.path.join(add,listsong[3]))   

                elif "exit" in data1:
                    speechtx("thank you")
                    break

                
                time.sleep(5)

    else:
        print("Thanks")