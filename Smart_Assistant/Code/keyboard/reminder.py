import time
from playsound import playsound
import os
from gtts import gTTS

playsound('Smart_Assistant/Sound/4.mp3')
r = input("What is it? ")
time.sleep(1)
playsound('Smart_Assistant/Sound/5.mp3')
t = input("How many minutes later should I show it? ")
t = int(t)
print("The reminder has been set")
playsound('Smart_Assistant/Sound/6.mp3')
time.sleep(t*60-7)
playsound('Smart_Assistant/Sound/Bell.mp3')
print("You have a reminder!")
playsound('Smart_Assistant/Sound/rem.mp3')
playsound('Smart_Assistant/Sound/8.mp3')
a = input("Would youlike to see the reminder?(yes/no) ")
if a == "yes":
    print("Your reminder is:")
    playsound('Smart_Assistant/Sound/9.mp3')
    print("")
    print(r)
    print("")
    tts = gTTS(text=r, lang='en')
    tts.save('Smart_Assistant/Sound/read.mp3')
    playsound('Smart_Assistant/Sound/read.mp3')
    os.remove("Smart_Assistant/Sound/read.mp3")
    import command
if a == "no":
    playsound('Smart_Assistant/Sound/7.mp3')
    import command