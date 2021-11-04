from random import randint
from playsound import playsound

# generate some integers
value = randint(1, 5)
if value == 1:
    print("Why do people take an extra pair of socks when they go golfing?")
    print("In case they get a hole in one!")
    playsound('Smart_Assistant/Sound/j1.mp3')
    playsound('Smart_Assistant/Sound/laugh.mp3')
    import main

if value == 2:
    print("What time is it when the clock strikes 13?")
    print("It's the time to get a new clock!")
    playsound('Smart_Assistant/Sound/j2.mp3')
    playsound('Smart_Assistant/Sound/laugh.mp3')
    import main

if value == 3:
    print("Where did the cat go when it lost it’s tail?")
    print("To the retail store!")
    playsound('Smart_Assistant/Sound/j3.mp3')
    playsound('Smart_Assistant/Sound/laugh.mp3')
    import main

if value == 4:
    print("Why can't a nose be 12 inches long?")
    print("Because then it would be a foot!")
    playsound('Smart_Assistant/Sound/j4.mp3')
    playsound('Smart_Assistant/Sound/laugh.mp3')
    import main

if value == 5:
    print("How do you make a squid laugh?")
    print("With Ten-Tickles!")
    playsound('Smart_Assistant/Sound/j5.mp3')
    playsound('Smart_Assistant/Sound/laugh.mp3')
    import main