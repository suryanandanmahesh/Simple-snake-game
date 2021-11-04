import time
from playsound import playsound

print("Hi! I am your personal assistant, nice to meet you!")
playsound('Smart_Assistant/Sound/1.mp3')
time.sleep(.7)
# These are the things you can say to the assistant
print("")
print("You can ask me things like:")
print("")
print("a)Play a game")
print("b)Set a reminder")
print("c)What's the weather")
print("d)Open calculator")
print("e)Convert text to speech")
print("f)More info")
print("")
playsound('Smart_Assistant/Sound/2.mp3')
import command