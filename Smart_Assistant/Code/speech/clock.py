import time
from playsound import playsound
from gtts import gTTS
import os

playsound('Smart_Assistant/Sound/tim.mp3')
t = time.strftime("%I:%M %p")
print(t)
tts = gTTS(text=t, lang='en')
tts.save('Smart_Assistant/Sound/read.mp3')
playsound('Smart_Assistant/Sound/read.mp3')
os.remove("Smart_Assistant/Sound/read.mp3")

import main