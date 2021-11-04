from playsound import playsound
import os
from gtts import gTTS
import speech_recognition as sr

r = sr.Recognizer()
playsound('Smart_Assistant/Sound/4.mp3')
print("")
te = input("What is it? ")
tts = gTTS(text = te, lang ='en')
tts.save("Smart_Assistant/Sound/sound.mp3")
playsound('Smart_Assistant/Sound/sound.mp3')
os.remove("Smart_Assistant/Sound/sound.mp3")
import main