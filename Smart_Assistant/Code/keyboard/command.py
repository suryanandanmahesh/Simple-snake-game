# importing modules
from playsound import playsound
import webbrowser

try:
    while True:
        
        playsound('Smart_Assistant/Sound/3.mp3')
        c = input("What would you like to do? ")
        if c == "what's is the weather":
            playsound('Smart_Assistant/Sound/we.mp3')
            import weather

        if c == "what is the weather":
            playsound('Smart_Assistant/Sound/we.mp3')
            import weather

        if c == "weather":
            playsound('Smart_Assistant/Sound/we.mp3')
            import weather

        if c == "c":
            playsound('Smart_Assistant/Sound/we.mp3')
            import weather

        if c == "a": # 'a' to play the snake game
            playsound('Smart_Assistant/Sound/7.mp3')
            import snake_game

        if c == "b": # Set a reminder
            import reminder

        if c == "d": # Calculator
            print("Ok")
            playsound('Smart_Assistant/Sound/7.mp3')
            import calculator

        if c == "play a game": # Snake game
            playsound('Smart_Assistant/Sound/7.mp3')
            import snake_game

        if c == "set a reminder": # Set a reminder

            playsound('Smart_Assistant/Sound/4.mp3')
            import reminder
        if c == "open calculator": # Calculator
            print("Ok")
            playsound('Smart_Assistant/Sound/7.mp3')
            import calculator

        if c == "game": # Snake game
            playsound('Smart_Assistant/Sound/7.mp3')
            import snake_game

        if c == "play": # Snake game
            playsound('Smart_Assistant/Sound/7.mp3')
            import snake_game

        if c == "reminder": # set a reminder
            print("Ok")
            playsound('Smart_Assistant/Sound/7.mp3')
            import reminder
            
        if c == "calculator": # Calculator
            print("Ok")
            playsound('Smart_Assistant/Sound/7.mp3')
            import calculator

        if c == "e": # Convert text to speech
            import text_to_speech

        if c == "convert text to speech": # Convert text to speech
            import text_to_speech

        if c == "text to speech": # Convert text to speech
            import text_to_speech

        if c == "f": # More info
            import info

        if c == "more info": # More info
            import info

        if c == "info": # More info
            import info

        if c == "more": # More info
            import info

        if c == "bye": # More info
            break

        if c == "goodbye": # More info
            break

        if c == "make me laugh": # joke
            playsound('Smart_Assistant/Sound/7.mp3')
            import joke

        if c == "tell a joke": # joke
            playsound('Smart_Assistant/Sound/7.mp3')
            import joke

        if c == "tell me a joke": # joke
            playsound('Smart_Assistant/Sound/7.mp3')
            import joke

        else:
            print("I found this on the web")
            playsound('Smart_Assistant/Sound/web.mp3')
            new = 2
            tabUrl = "https://www.google.com/search?q="
            term = c
            webbrowser.open(tabUrl+term,new=new)

finally:
    playsound('Smart_Assistant/Sound/bye.mp3')
    print("OK")