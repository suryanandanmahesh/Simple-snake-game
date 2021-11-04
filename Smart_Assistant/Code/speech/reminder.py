import time
from playsound import playsound
import os
from gtts import gTTS
import speech_recognition as sr
os.system('CLS')

r = sr.Recognizer()

with sr.Microphone() as source:
    playsound('Smart_Assistant/Sound/4.mp3')
    print("What is it? ")
    au = r.listen(source)
    try:
        s = r.recognize_google(au)
        print(s)
    except:
        print("Sorry could not recognize what you said")
time.sleep(1)
playsound('Smart_Assistant/Sound/5.mp3')
print("How many minutes later should I show it? ")
with sr.Microphone() as source:
    au = r.listen(source)
    try:
        t = r.recognize_google(au)
        print(t)
        t = int(t)
    except:
        print("Sorry could not recognize what you said")
print("The reminder has been set")
playsound('Smart_Assistant/Sound/6.mp3')
time.sleep(t*60-7)
playsound('Smart_Assistant/Sound/Bell.mp3')
print("You have a reminder!")
playsound('Smart_Assistant/Sound/rem.mp3')
playsound('Smart_Assistant/Sound/8.mp3')
print("Would youlike to see the reminder?(yes/no) ")
with sr.Microphone() as source:
    au = r.listen(source)
    try:
        a = r.recognize_google(au)
        print(a)
    except:
        print("Sorry could not recognize what you said")
if a == "yes":
    print("Your reminder is:")
    playsound('Smart_Assistant/Sound/9.mp3')
    print("")
    print(s)
    print("")
    tts = gTTS(text=s, lang='en')
    tts.save('Smart_Assistant/Sound/read.mp3')
    playsound('Smart_Assistant/Sound/read.mp3')
    os.remove("Smart_Assistant/Sound/read.mp3")
    import main

if a == "no":
    playsound('Smart_Assistant/Sound/7.mp3')
    import main