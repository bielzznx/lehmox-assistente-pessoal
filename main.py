# our main file

import speech_recognition as sr 

r = sr.recognizer()

with sr.microphone() as source:
    audio = r.listen(source)

    print(r.recognize_google(audio))