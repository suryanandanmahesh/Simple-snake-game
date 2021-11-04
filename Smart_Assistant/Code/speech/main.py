# importing modules
import time
from playsound import playsound
import speech_recognition as sr
import webbrowser
import os
c = "initial_val"

r = sr.Recognizer()
os.system('CLS')
a = 1

while a == 1: # Keep looping as long as a = 1
    rec = "initial_val"
    with sr.Microphone() as source:
        os.system('CLS')
        print("Smart_Assistant")
        audio = r.listen(source)
        try:
            rec = r.recognize_google(audio)
            print(rec)
        except:
            print("")
            
    search_keywords=['Bob','Bobby'] # Wake word
    for word in search_keywords:
        if word in rec:
            a = 0 # Changes the value of a to break the loop

'''/////////////Main code////////////////'''

os.system('CLS')
c = "initial_val"
with sr.Microphone() as source:
    os.system('CLS')
    print(".....")
    playsound('Smart_Assistant/Sound/start.mp3')
    au = r.listen(source)
    try:
        c = r.recognize_google(au)
        print(c)
    except:
        print("Sorry could not recognize what you said")
        time.sleep(1)
        import main

search_keywords=['time','clock'] 
# Search for the key word
for word in search_keywords:
    if word in c:
        import clock

search_keywords=['weather','forcast','report'] # Search for the key word
for word in search_keywords:
    if word in c:
        import weather

search_keywords=['game','play'] # Search for the key word
for word in search_keywords:
    if word in c:
        playsound('Smart_Assistant/Sound/7.mp3')
        import snake_game

search_keywords=['remind','reminder'] # Search for the key word
for word in search_keywords:
    if word in c:
        import reminder

search_keywords=['calculate','calculator'] # Search for the key word
for word in search_keywords:
    if word in c:
        playsound('Smart_Assistant/Sound/alright.mp3')
        import calculator

search_keywords=['text','speech'] # Search for the key word
for word in search_keywords:
    if word in c:
        playsound('Smart_Assistant/Sound/7.mp3')
        import text_to_speech

search_keywords=['bye','goodbye'] # Search for the key word
for word in search_keywords:
    if word in c:
        print("Goodbye")
        playsound('Smart_Assistant/Sound/bye.mp3')

search_keywords=['joke','laugh','funny'] # Search for the key word
for word in search_keywords:
    if word in c:
        playsound('Smart_Assistant/Sound/alright.mp3')
        import joke

search_keywords=['search'] # Search for the key word
for word in search_keywords:
    if word in c:
        term = c.replace('search ','')
        playsound('Smart_Assistant/Sound/web.mp3')
        new = 2
        tabUrl = "https://www.google.com/search?q="
        webbrowser.open(tabUrl+term,new=new)
        c = "initial_val"

if c == "initial_val":
    import main

else:
    playsound('Smart_Assistant/Sound/10.mp3')
    import main

import main