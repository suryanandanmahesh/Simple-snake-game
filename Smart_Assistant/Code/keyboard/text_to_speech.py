from playsound import playsound
import os
from gtts import gTTS
os.system('CLS')

playsound('Smart_Assistant/Sound/4.mp3')
print("")
te = input("What is it? ")
print("")
tts = gTTS(text=te, lang='en')
tts.save("Smart_Assistant/Sound/sound.mp3")
playsound('Smart_Assistant/Sound/sound.mp3')
os.remove("Smart_Assistant/Sound/sound.mp3")
import command