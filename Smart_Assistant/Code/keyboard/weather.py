import requests
from playsound import playsound
from gtts import gTTS
import os
os.system('CLS')

# API base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# City Name
CITY = "Dubai"

# Your API key
API_KEY = "5dae5a15d457a6c326215c156f1083b3"

# updating the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL)

# checking the status code of the request
if response.status_code == 200:
   # retrieving data in the json format
   data = response.json()
   # take the main dict block
   main = data['main']
   # weather report
   weather_report = data['weather']
   weather = (f"Today's Weather forcast is: {weather_report[0]['description']}")
   print("")
   print(weather)
   print("")
   
   tts = gTTS(text=weather, lang='en')
   tts.save('Smart_Assistant/Sound/read.mp3')
   playsound('Smart_Assistant/Sound/read.mp3')
   os.remove("Smart_Assistant/Sound/read.mp3")
   import main
else:
   # showing the error message
   print("Error in the HTTP request")
   import main