# our main file

import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
    while true:
    audio = r.listen(source)

        print(r.recognize_google(audio))